"""Aggregate ontology gaps across articles."""

from __future__ import annotations

from collections import defaultdict

from .ontology_grounder import GroundingDecision, normalize_label

PARENT_SUGGESTIONS = {
    "management_intervention": "ELMO biological ecosystem management process",
    "environmental_process": "ELMO environmental process",
    "environmental_variable": "ELMO environmental variable",
    "variable": "ELMO environmental variable or PATO quality",
    "taxon": "Wikidata taxon",
}


class GapReport:
    def __init__(self, ontology_sources: dict | None = None):
        self._records: dict[tuple[str, str], dict] = defaultdict(dict)
        self.ontology_sources = ontology_sources or {}

    def add(self, decision: GroundingDecision, source: dict, node_id: str = "") -> None:
        if decision.status in {"exact_match", "synonym_match"}:
            return
        key = (decision.semantic_role, normalize_label(decision.mention))
        record = self._records.get(key) or {
            "term": decision.mention,
            "semantic_role": decision.semantic_role,
            "status": decision.status,
            "target_ontologies": decision.searched_ontologies,
            "proposed_label": decision.mention,
            "proposed_definition": (
                f"A {decision.semantic_role.replace('_', ' ')} corresponding "
                f"to '{decision.mention}'."
            ),
            "candidate_parent": PARENT_SUGGESTIONS.get(decision.semantic_role),
            "review_confidence": 0.5 if decision.candidates else 0.8,
            "candidate_matches": [
                candidate.to_dict() for candidate in decision.candidates
            ],
            "lookup_errors": decision.errors,
            "occurrences": [],
            "article_count": 0,
        }
        occurrence = {
            "doi": source.get("doi"),
            "title": source.get("title"),
            "node_id": node_id,
            "evidence_text": decision.evidence_text,
        }
        if occurrence not in record["occurrences"]:
            record["occurrences"].append(occurrence)
        record["article_count"] = len(
            {item.get("doi") or item.get("title") for item in record["occurrences"]}
        )
        record["occurrence_count"] = len(record["occurrences"])
        if decision.status == "lookup_error":
            record["status"] = "lookup_error"
        self._records[key] = record

    def to_dict(self) -> dict:
        records = sorted(
            self._records.values(),
            key=lambda item: (
                -item["article_count"],
                item["semantic_role"],
                item["term"].casefold(),
            ),
        )
        return {
            "report_version": "1.0",
            "description": (
                "Literature terms without accepted matches in their preferred "
                "ontologies."
            ),
            "ontology_sources": self.ontology_sources,
            "gaps": records,
        }
