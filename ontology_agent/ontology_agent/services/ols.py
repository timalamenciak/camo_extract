"""OLS (Ontology Lookup Service) API client.

Supports OLS API v2, searching across all ontologies or specific ones.
"""

from __future__ import annotations

from typing import Any, Optional

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import (
    HierarchyInfo,
    OntologySource,
    OntologyTermResult,
)


class OLSClient:
    """Client for the EBI Ontology Lookup Service API.

    OLS provides REST API endpoints for searching ontology terms,
    retrieving term details, and navigating hierarchy relationships.

    API documentation: https://www.ebi.ac.uk/ols/docs/api
    """

    DEFAULT_ENDPOINT = "https://www.ebi.ac.uk/ols/api"

    def __init__(self, endpoint: Optional[str] = None, timeout: int = 30):
        self.endpoint = endpoint or self.DEFAULT_ENDPOINT
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "ontology-agent/0.1.0 (EcoWeaver; tim.alamenciak@gmail.com)",
            }
        )

    def search(
        self,
        query: str,
        ontology: Optional[str] = None,
        limit: int = 10,
        fields: Optional[list[str]] = None,
        search_synonyms: bool = True,
    ) -> list[dict[str, Any]]:
        """Search for terms in OLS.

        Args:
            query: Search query string
            ontology: Optional ontology prefix (e.g., "ENVO")
            limit: Maximum number of results
            fields: Optional list of fields to return
            search_synonyms: Whether to search in synonyms

        Returns:
            List of term search results
        """
        params = {
            "q": query,
            "rows": limit * 2,
            "offset": 0,
            "fieldList": (
                ",".join(fields)
                if fields
                else "iri,label,description,ontology_name,curie"
            ),
        }

        if ontology:
            params["ontology"] = ontology

        if search_synonyms:
            params["queryFields"] = "label,synonym,description"

        response = self._get("/search", params)
        if not response:
            return []

        terms = response.get("_embedded", {}).get("terms", [])
        if not terms:
            terms = response.get("response", {}).get("docs", [])

        sorted_terms = self._sort_by_specificity(terms)

        return sorted_terms[:limit]

    def get_term(
        self,
        ontology: str,
        term_id: str,
        include_ancestors: bool = False,
    ) -> Optional[dict[str, Any]]:
        """Retrieve detailed information about a specific term.

        Args:
            ontology: Ontology prefix (e.g., "ENVO")
            term_id: Term ID (e.g., "00001001")
            include_ancestors: Whether to include ancestor information

        Returns:
            Term details or None if not found
        """
        params = {}
        if include_ancestors:
            params["includeAncient"] = "true"

        response = self._get(f"/ontologies/{ontology}/terms/{term_id}", params)
        return response

    def get_ancestors(
        self,
        ontology: str,
        term_id: str,
    ) -> list[dict[str, Any]]:
        """Get ancestor terms for a given term.

        Args:
            ontology: Ontology prefix
            term_id: Term ID

        Returns:
            List of ancestor terms
        """
        response = self._get(f"/ontologies/{ontology}/terms/{term_id}/ancestors")
        if not response:
            return []

        return response.get("_embedded", {}).get("terms", [])

    def get_ontology_info(self, ontology: str) -> Optional[dict[str, Any]]:
        """Get information about an ontology.

        Args:
            ontology: Ontology prefix

        Returns:
            Ontology metadata or None if not found
        """
        response = self._get(f"/ontologies/{ontology}")
        return response

    def _get(self, path: str, params: Optional[dict] = None) -> Optional[dict]:
        """Make a GET request to the OLS API with retry logic."""
        url = f"{self.endpoint.rstrip('/')}/{path.lstrip('/')}"

        @retry(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=1, max=10),
            reraise=True,
        )
        def _request():
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    return None
                raise
            except requests.exceptions.RequestException:
                raise

        try:
            return _request()
        except Exception:
            return None

    def _sort_by_specificity(self, terms: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Sort terms by specificity (more specific terms first).

        More specific terms typically have:
        - More ancestors in the hierarchy
        - Are further from root nodes

        Args:
            terms: List of term data from API

        Returns:
            Terms sorted by specificity (most specific first)
        """

        def specificity_score(term: dict[str, Any]) -> int:
            ancestors = term.get("ancestors", [])
            if isinstance(ancestors, list):
                return len(ancestors)
            return 0

        return sorted(terms, key=specificity_score, reverse=True)

    def _iri_to_curie(self, iri: str) -> Optional[str]:
        """Convert IRI to CURIE format.

        Args:
            iri: Full IRI string (e.g., http://purl.obolibrary.org/obo/ENVO_00001001)

        Returns:
            CURIE string (e.g., ENVO:00001001) or None if conversion fails
        """
        if not iri:
            return None

        # Try to extract prefix from common OWL/OLB patterns
        if "/obo/" in iri:
            parts = iri.split("/obo/")
            if len(parts) > 1:
                remainder = parts[1]
                if "_" in remainder:
                    prefix = remainder.split("_")[0]
                    id_part = remainder.split("_")[1]
                    return f"{prefix}:{id_part}"

        return None

    def to_term_result(
        self,
        term_data: dict[str, Any],
        include_hierarchy: bool = True,
    ) -> Optional[OntologyTermResult]:
        """Convert OLS API response to OntologyTermResult model.

        Args:
            term_data: Raw API response data
            include_hierarchy: Whether to fetch hierarchy info

        Returns:
            Parsed OntologyTermResult or None if invalid
        """
        try:
            curie = term_data.get("curie")

            if not curie or ":" not in curie:
                iri = term_data.get("iri", "")
                if iri:
                    curie = self._iri_to_curie(iri)

            if not curie or ":" not in curie:
                return None

            prefix = curie.split(":")[0]

            hierarchy_info = None
            if include_hierarchy:
                hierarchy_info = self._build_hierarchy_info(term_data, prefix)

            return OntologyTermResult(
                curie=curie,
                prefix=prefix,
                label=term_data.get("label", curie),
                definition=(
                    term_data.get("description", [None])[0]
                    if term_data.get("description")
                    else None
                ),
                synonyms=term_data.get("synonym", []),
                source=OntologySource.OLS,
                ontology=term_data.get("ontology_name", prefix.lower()),
                hierarchy=hierarchy_info,
                metadata={
                    "is_defining_ontology": term_data.get(
                        "is_defining_ontology", False
                    ),
                    "url": term_data.get("iri", ""),
                },
            )
        except (KeyError, TypeError):
            return None

    def _build_hierarchy_info(
        self,
        term_data: dict[str, Any],
        ontology: str,
    ) -> Optional[HierarchyInfo]:
        """Build HierarchyInfo from term data."""
        curie = term_data.get("curie", term_data.get("iri", ""))
        if ":" not in curie:
            return None

        ancestors = []
        if "ancestors" in term_data:
            for a in term_data["ancestors"]:
                if ":" in a:
                    ancestors.append(a)

        bfo_class = self._detect_bfo_class(term_data, ancestors)

        return HierarchyInfo(
            curie=curie,
            label=term_data.get("label", curie),
            ancestors=ancestors,
            bfo_class=bfo_class,
            depth=len(ancestors),
        )

    def _detect_bfo_class(
        self,
        term_data: dict[str, Any],
        ancestors: list[str],
    ) -> Optional[str]:
        """Detect the highest-level BFO class for a term.

        Args:
            term_data: Term details
            ancestors: List of ancestor CURIEs

        Returns:
            BFO class CURIE if detected, None otherwise
        """
        bfo_prefixes = {
            "BFO:0000002": "continuant",
            "BFO:0000003": "occurrent",
        }

        for ancestor in ancestors:
            if ancestor.startswith("BFO:") and ancestor in bfo_prefixes:
                return ancestor

        return None

    def get_preferred_ontology(
        self,
        query: str,
        candidates: list[dict[str, Any]],
    ) -> Optional[str]:
        """Suggest the most appropriate ontology for a query.

        Args:
            query: Search query
            candidates: Candidate term results

        Returns:
            Preferred ontology prefix or None
        """
        if not candidates:
            return None

        ontology_counts: dict[str, int] = {}
        for term in candidates:
            ont = term.get("ontology_name", "unknown")
            ontology_counts[ont] = ontology_counts.get(ont, 0) + 1

        if ontology_counts:
            max_count = max(ontology_counts.values())
            for k, v in ontology_counts.items():
                if v == max_count:
                    return k

        return None


def get_ols_client(timeout: int = 30) -> OLSClient:
    """Create and return an OLSClient instance."""
    return OLSClient(timeout=timeout)


def search_ols(
    query: str,
    preferred_ontology: Optional[str] = None,
    limit: int = 10,
    timeout: int = 30,
    search_synonyms: bool = True,
) -> tuple[list[OntologyTermResult], Optional[str]]:
    """Search OLS and return results.

    Args:
        query: Search query
        preferred_ontology: Optional preferred ontology
        limit: Maximum results
        timeout: Request timeout
        search_synonyms: Whether to search in synonyms

    Returns:
        Tuple of (results, suggested_ontology)
    """
    client = get_ols_client(timeout=timeout)

    search_ontologies = [preferred_ontology] if preferred_ontology else []

    results: list[OntologyTermResult] = []

    if search_ontologies:
        for ontology in search_ontologies:
            terms = client.search(
                query, ontology=ontology, limit=limit, search_synonyms=search_synonyms
            )
            for term_data in terms:
                result = client.to_term_result(term_data)
                if result:
                    results.append(result)
            if results:
                break

    if not results:
        terms = client.search(query, limit=limit * 2, search_synonyms=search_synonyms)
        suggested = client.get_preferred_ontology(query, terms)
        for term_data in terms:
            result = client.to_term_result(term_data)
            if result:
                results.append(result)

    if not results and search_ontologies:
        return [], preferred_ontology

    suggested = None
    if not results:
        terms = client.search(query, limit=limit * 2, search_synonyms=search_synonyms)
        suggested = client.get_preferred_ontology(query, terms)

    return results, suggested
