"""Typed ontology grounding with auditable match decisions."""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from typing import Iterable, Optional
from urllib.parse import unquote

import requests
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

USER_AGENT = "camo-extract/0.2 (https://github.com/timalamenciak/camo_extract)"
OBO_SYNONYM = URIRef("http://www.geneontology.org/formats/oboInOwl#hasExactSynonym")


def normalize_label(value: str) -> str:
    """Normalize labels for conservative exact/synonym matching."""
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


@dataclass
class OntologyCandidate:
    curie: str
    label: str
    ontology: str
    iri: str = ""
    synonyms: list[str] = field(default_factory=list)
    definition: Optional[str] = None
    score: float = 0.0
    match_type: str = "close_match_needs_review"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class GroundingDecision:
    mention: str
    semantic_role: str
    status: str
    searched_ontologies: list[str]
    accepted: Optional[OntologyCandidate] = None
    candidates: list[OntologyCandidate] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    evidence_text: str = ""

    def to_dict(self) -> dict:
        data = asdict(self)
        return data


class OLSClient:
    """Small OLS4 client that never broadens an ontology-restricted query."""

    def __init__(self, endpoint: str, timeout: int = 30):
        self.endpoint = endpoint.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json", "User-Agent": USER_AGENT}
        )

    def search(
        self, query: str, ontology: str, limit: int = 10
    ) -> list[OntologyCandidate]:
        params: dict[str, str | int] = {
            "q": query,
            "ontology": ontology.lower(),
            "queryFields": "label,synonym",
            "fieldList": (
                "iri,label,description,ontology_name,ontology_prefix,curie,"
                "obo_id,short_form,synonym,obo_synonym"
            ),
            "local": "true",
            "obsoletes": "false",
            "rows": limit,
        }
        response = self.session.get(
            f"{self.endpoint}/search", params=params, timeout=self.timeout
        )
        response.raise_for_status()
        payload = response.json()
        terms = payload.get("_embedded", {}).get("terms", [])
        if not terms:
            terms = payload.get("response", {}).get("docs", [])
        return [
            candidate
            for term in terms
            if (candidate := self._candidate(term, ontology))
        ]

    def _candidate(self, term: dict, ontology: str) -> Optional[OntologyCandidate]:
        iri = term.get("iri", "")
        curie = term.get("curie") or term.get("obo_id") or term.get("short_form")
        if curie and "_" in curie and ":" not in curie:
            prefix, identifier = curie.split("_", 1)
            curie = f"{prefix}:{identifier}"
        if not curie and "/obo/" in iri:
            short = unquote(iri).rsplit("/obo/", 1)[-1]
            if "_" in short:
                prefix, identifier = short.split("_", 1)
                curie = f"{prefix}:{identifier}"
        if not curie:
            return None
        synonyms = term.get("synonym") or term.get("obo_synonym") or []
        if isinstance(synonyms, str):
            synonyms = [synonyms]
        description = term.get("description")
        if isinstance(description, list):
            description = description[0] if description else None
        return OntologyCandidate(
            curie=curie,
            label=term.get("label") or curie,
            ontology=(
                term.get("ontology_prefix") or term.get("ontology_name") or ontology
            ).upper(),
            iri=iri,
            synonyms=synonyms,
            definition=description,
        )


class ELMOClient:
    """Load and search the released ELMO OWL graph."""

    def __init__(self, url: str, timeout: int = 30):
        self.url = url
        self.timeout = timeout
        self._terms: Optional[list[OntologyCandidate]] = None

    def search(self, query: str, limit: int = 10) -> list[OntologyCandidate]:
        if self._terms is None:
            self._terms = self._load_terms()
        query_norm = normalize_label(query)
        results = []
        for term in self._terms:
            labels = [term.label, *term.synonyms]
            if any(
                query_norm in normalize_label(label)
                or normalize_label(label) in query_norm
                for label in labels
            ):
                results.append(term)
        return sorted(
            results, key=lambda item: _candidate_score(query, item), reverse=True
        )[:limit]

    def _load_terms(self) -> list[OntologyCandidate]:
        response = requests.get(
            self.url, timeout=self.timeout, headers={"User-Agent": USER_AGENT}
        )
        response.raise_for_status()
        graph = Graph()
        last_error = None
        for fmt in ("xml", "turtle", None):
            try:
                graph.parse(data=response.content, format=fmt, publicID=response.url)
                break
            except (
                Exception
            ) as exc:  # pragma: no cover - depends on remote serialization
                last_error = exc
                graph = Graph()
        else:
            raise RuntimeError(f"Could not parse ELMO ontology: {last_error}")

        terms = []
        for subject in set(graph.subjects(RDF.type, OWL.Class)):
            label = graph.value(subject, RDFS.label)
            if not label:
                continue
            synonyms = {
                str(value)
                for predicate in (SKOS.altLabel, OBO_SYNONYM)
                for value in graph.objects(subject, predicate)
            }
            iri = str(subject)
            identifier = iri.rsplit("/", 1)[-1].rsplit("#", 1)[-1]
            if identifier.lower().startswith("elmo_"):
                identifier = identifier.split("_", 1)[1]
            terms.append(
                OntologyCandidate(
                    curie=f"ELMO:{identifier}",
                    label=str(label),
                    ontology="ELMO",
                    iri=iri,
                    synonyms=sorted(synonyms),
                )
            )
        return terms


class WikidataClient:
    """Wikidata entity search for taxon mentions."""

    def __init__(self, endpoint: str, timeout: int = 30):
        self.endpoint = endpoint
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def search(self, query: str, limit: int = 10) -> list[OntologyCandidate]:
        params: dict[str, str | int] = {
            "action": "wbsearchentities",
            "search": query,
            "language": "en",
            "uselang": "en",
            "type": "item",
            "limit": limit,
            "format": "json",
            "origin": "*",
        }
        response = self.session.get(
            self.endpoint,
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        candidates = []
        for item in response.json().get("search", []):
            description = item.get("description", "")
            aliases = item.get("aliases", [])
            if isinstance(aliases, str):
                aliases = [aliases]
            candidate = OntologyCandidate(
                curie=f"WD:{item['id']}",
                label=item.get("label") or item["id"],
                ontology="WIKIDATA",
                iri=item.get(
                    "concepturi", f"https://www.wikidata.org/entity/{item['id']}"
                ),
                synonyms=aliases,
                definition=description,
            )
            # Reject obvious non-taxa even when their label happens to match.
            taxon_words = (
                "taxon",
                "species",
                "genus",
                "family",
                "organism",
                "plant",
                "animal",
            )
            if any(word in description.casefold() for word in taxon_words):
                candidates.append(candidate)
        return candidates


def _candidate_score(query: str, candidate: OntologyCandidate) -> float:
    query_norm = normalize_label(query)
    label_norm = normalize_label(candidate.label)
    if label_norm == query_norm:
        candidate.score = 1.0
        candidate.match_type = "exact_match"
        return candidate.score
    if any(normalize_label(synonym) == query_norm for synonym in candidate.synonyms):
        candidate.score = 0.98
        candidate.match_type = "synonym_match"
        return candidate.score
    candidate.score = round(SequenceMatcher(None, query_norm, label_norm).ratio(), 4)
    candidate.match_type = "close_match_needs_review"
    return candidate.score


class OntologyGrounder:
    """Route mentions by CAMO entity type and retain every lookup decision."""

    ROUTES = {
        "taxon": ["WIKIDATA"],
        "management_intervention": ["ELMO"],
        "environmental_process": ["ELMO", "ENVO"],
        "environmental_variable": ["ELMO", "ENVO"],
    }
    ATTRIBUTE_ROUTE = ["ELMO", "PATO"]

    def __init__(
        self,
        ols_endpoint: str,
        elmo_url: str,
        wikidata_endpoint: str,
        timeout: int = 30,
        review_threshold: float = 0.7,
    ):
        self.ols = OLSClient(ols_endpoint, timeout)
        self.elmo = ELMOClient(elmo_url, timeout)
        self.wikidata = WikidataClient(wikidata_endpoint, timeout)
        self.review_threshold = review_threshold

    def ground(
        self, mention: str, semantic_role: str, route: Iterable[str]
    ) -> GroundingDecision:
        mention = mention.strip()
        searched = list(route)
        candidates: list[OntologyCandidate] = []
        errors: list[str] = []
        for ontology in searched:
            try:
                if ontology == "ELMO":
                    found = self.elmo.search(mention)
                elif ontology == "WIKIDATA":
                    found = self.wikidata.search(mention)
                else:
                    found = self.ols.search(mention, ontology)
                for candidate in found:
                    _candidate_score(mention, candidate)
                candidates.extend(found)
                accepted = next(
                    (
                        candidate
                        for candidate in found
                        if candidate.match_type in {"exact_match", "synonym_match"}
                    ),
                    None,
                )
                if accepted:
                    return GroundingDecision(
                        mention,
                        semantic_role,
                        accepted.match_type,
                        searched,
                        accepted,
                        candidates,
                        errors,
                    )
            except Exception as exc:
                errors.append(f"{ontology}: {type(exc).__name__}: {exc}")
        candidates.sort(key=lambda item: item.score, reverse=True)
        status = (
            "lookup_error"
            if errors and len(errors) == len(searched)
            else (
                "close_match_needs_review"
                if candidates and candidates[0].score >= self.review_threshold
                else "no_match"
            )
        )
        return GroundingDecision(
            mention, semantic_role, status, searched, None, candidates[:10], errors
        )

    def ground_node(self, node: dict) -> tuple[dict, list[GroundingDecision]]:
        node = dict(node)
        entity_type = node.get("entity_type", "environmental_variable")
        entity_mention = str(
            node.pop("entity_mention", "")
            or node.pop("entity_label", "")
            or node.get("entity_term", "")
            or node.get("name", "")
        )
        attribute_mention = str(
            node.pop("measured_attribute_mention", "")
            or node.pop("attribute_label", "")
            or node.pop("attribute", "")
            or node.get("measured_attribute", "")
        )
        decisions = []
        entity_decision = self.ground(
            entity_mention, entity_type, self.ROUTES.get(entity_type, ["ELMO", "ENVO"])
        )
        decisions.append(entity_decision)
        if entity_decision.accepted:
            node["entity_term"] = entity_decision.accepted.curie
        else:
            digest = hashlib.sha1(
                f"{entity_type}:{entity_mention}".encode("utf-8")
            ).hexdigest()[:10]
            node["entity_term"] = f"causal_mosaic:unresolved_{digest}"
        if attribute_mention:
            attribute_decision = self.ground(
                attribute_mention, "variable", self.ATTRIBUTE_ROUTE
            )
            decisions.append(attribute_decision)
            node["measured_attribute"] = (
                attribute_decision.accepted.curie
                if attribute_decision.accepted
                else attribute_mention
            )
        spans = node.get("source_spans", [])
        evidence_text = (
            spans[0].get("text", "") if spans and isinstance(spans[0], dict) else ""
        )
        for decision in decisions:
            decision.evidence_text = evidence_text
        node.setdefault("name", entity_mention)
        return node, decisions
