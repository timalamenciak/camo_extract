"""Custom ontology loader for OWL files not listed on OLS/BioPortal.

Supports loading ontologies from remote OWL files via URL.
"""

from __future__ import annotations

import time
from typing import Optional

import requests
from rdflib import RDF, RDFS, Graph, Literal, Namespace

from ..models import (
    HierarchyInfo,
    OntologySource,
    OntologyTermResult,
)


class CustomOntologyClient:
    """Client for loading and searching custom OWL ontologies."""

    def __init__(self, url: str, name: str, prefix: str, timeout: int = 30):
        self.url = url
        self.name = name
        self.prefix = prefix
        self.timeout = timeout
        self._term_cache: dict[str, OntologyTermResult] = {}
        self._load_time: Optional[float] = None

    def load_ontology(self) -> bool:
        """Load ontology from URL.

        Returns:
            True if URL is accessible, False otherwise
        """
        try:
            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()
            self._load_time = time.time()
            return True
        except Exception:
            return False

    def search(self, query: str, limit: int = 10) -> list[OntologyTermResult]:
        """Search the custom ontology for matching terms.

        Args:
            query: Search query (case-insensitive substring match)
            limit: Maximum results

        Returns:
            List of matching terms
        """
        if self._load_time is None:
            loaded = self.load_ontology()
            if not loaded:
                return []

        if not self._term_cache:
            self._build_cache()

        results = []
        query_lower = query.lower()
        for term in self._term_cache.values():
            if query_lower in term.label.lower():
                results.append(term)

        sorted_results = self._sort_results_by_specificity(results)
        return sorted_results[:limit]

    def _sort_results_by_specificity(
        self, results: list[OntologyTermResult]
    ) -> list[OntologyTermResult]:
        """Sort results by specificity (more specific terms first).

        Args:
            results: List of term results

        Returns:
            Sorted list (most specific first)
        """

        def specificity_score(term: OntologyTermResult) -> int:
            if term.hierarchy and term.hierarchy.ancestors:
                return len(term.hierarchy.ancestors)
            return 0

        return sorted(results, key=specificity_score, reverse=True)

    def get_term(self, term_id: str) -> Optional[OntologyTermResult]:
        """Get a specific term by ID.

        Args:
            term_id: Term ID (without prefix)

        Returns:
            Term details or None
        """
        if self._load_time is None:
            loaded = self.load_ontology()
            if not loaded:
                return None

        if not self._term_cache:
            self._build_cache()

        key = f"{self.prefix}:{term_id}"
        return self._term_cache.get(key)

    def _build_cache(self) -> None:
        """Build term cache from OWL file by parsing with rdflib."""
        try:
            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()

            g = Graph()
            g.parse(data=response.text, format="xml")

            OWL = Namespace("http://www.w3.org/2002/07/owl#")

            seen = set()
            for subject, predicate, obj in g.triples((None, RDF.type, OWL.Class)):
                label = g.value(subject, RDFS.label)
                if label and isinstance(label, Literal):
                    term_id = (
                        str(subject).split("#")[-1]
                        if "#" in str(subject)
                        else str(subject).split("/")[-1]
                    )

                    if term_id in seen:
                        continue
                    seen.add(term_id)

                    curie = f"{self.prefix}:{term_id}"

                    IAO = Namespace("http://purl.obolibrary.org/obo/")
                    definition = g.value(subject, IAO["IAO_0000115"])

                    ancestors = []
                    for _, pred, obj in g.triples((subject, None, None)):
                        if str(pred).endswith("subClassOf") and str(obj).startswith(
                            "http"
                        ):
                            ancestors.append(str(obj))

                    hierarchy_info = None
                    if ancestors:
                        hierarchy_info = HierarchyInfo(
                            curie=curie,
                            label=str(label),
                            ancestors=ancestors,
                            bfo_class=None,
                            depth=len(ancestors),
                        )

                    self._term_cache[curie] = OntologyTermResult(
                        label=str(label),
                        curie=curie,
                        prefix=self.prefix,
                        ontology=self.name,
                        definition=(
                            str(definition)
                            if definition and isinstance(definition, Literal)
                            else None
                        ),
                        source=OntologySource.OLS,
                        synonyms=[],
                        hierarchy=hierarchy_info,
                    )

            self._load_time = time.time()

        except Exception:
            self._term_cache = {}


def get_custom_client(
    url: str, name: str, prefix: str, timeout: int = 30
) -> CustomOntologyClient:
    """Create and return a CustomOntologyClient instance."""
    return CustomOntologyClient(url=url, name=name, prefix=prefix, timeout=timeout)


def search_custom_ontology(
    query: str,
    name: str,
    url: str,
    prefix: str,
    limit: int = 10,
    timeout: int = 30,
) -> list[OntologyTermResult]:
    """Search a custom ontology.

    Args:
        query: Search query
        name: Ontology name
        url: URL to OWL file
        prefix: Ontology prefix
        limit: Maximum results
        timeout: Request timeout

    Returns:
        List of matching terms
    """
    client = get_custom_client(url=url, name=name, prefix=prefix, timeout=timeout)

    if not client.load_ontology():
        return []

    return client.search(query, limit=limit)
