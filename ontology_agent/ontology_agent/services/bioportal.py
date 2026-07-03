"""BioPortal API client.

BioPortal is NIH-funded ontology repository with REST API access.
Requires an API key for most operations.

API documentation: https://www.bioontology.org/wiki/REST_API
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


class BioPortalClient:
    """Client for the BioPortal REST API.

    BioPortal provides web-based services for ontology representation,
    storage, and sharing. Requires API key for authenticated requests.

    API key can be obtained at: https://bioportal.bioontology.org/accounts/new
    """

    DEFAULT_ENDPOINT = "https://data.bioportal.bioontology.org"

    def __init__(self, api_key: Optional[str] = None, timeout: int = 30):
        self.endpoint = self.DEFAULT_ENDPOINT
        self.api_key = api_key or self._load_api_key()
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Authorization": f"apikey token={self.api_key}" if self.api_key else "",
                "User-Agent": "ontology-agent/0.1.0 (EcoWeaver; tim.alamenciak@gmail.com)",
            }
        )

    def _load_api_key(self) -> Optional[str]:
        """Load API key from environment if available."""
        import os

        return os.environ.get("BIOPORTAL_API_KEY")

    def search(
        self,
        query: str,
        ontologies: Optional[list[str]] = None,
        limit: int = 10,
        include: Optional[str] = None,
        search_synonyms: bool = True,
    ) -> list[dict[str, Any]]:
        """Search for terms in BioPortal.

        Args:
            query: Search query string
            ontologies: Optional list of ontology acronyms (e.g., ["ENVO"])
            limit: Maximum number of results
            include: Comma-separated list of additional data to include
            search_synonyms: Whether to search in synonyms

        Returns:
            List of term search results
        """
        params = {
            "query": query,
            "pagesize": limit * 2,
            "page": 1,
        }

        if ontologies:
            params["ontologies"] = ",".join(ontologies)

        if include:
            params["include"] = include

        if search_synonyms:
            params["querySearchMethod"] = "FULLTEXT"

        response = self._get("/search", params)
        if not response:
            return []

        terms = response.get("collection", [])

        sorted_terms = self._sort_by_specificity(terms)

        return sorted_terms[:limit]

    def get_term(
        self,
        ontology: str,
        term_id: str,
    ) -> Optional[dict[str, Any]]:
        """Retrieve detailed information about a specific term.

        Args:
            ontology: Ontology acronym (e.g., "ENVO")
            term_id: Term ID (e.g., "ENVO_00001001")

        Returns:
            Term details or None if not found
        """
        response = self._get(f"/ontologies/{ontology}/terms/{term_id}")
        return response

    def get_ontologies(
        self,
        query: Optional[str] = None,
    ) -> list[dict[str, Any]]:
        """List available ontologies.

        Args:
            query: Optional search query to filter ontologies

        Returns:
            List of ontology metadata
        """
        params = {}
        if query:
            params["query"] = query

        response = self._get("/ontologies", params)
        if not response:
            return []

        return response.get("collection", [])

    def get_ontology_info(self, ontology: str) -> Optional[dict[str, Any]]:
        """Get information about an ontology.

        Args:
            ontology: Ontology acronym

        Returns:
            Ontology metadata or None if not found
        """
        response = self._get(f"/ontologies/{ontology}")
        return response

    def _get(self, path: str, params: Optional[dict] = None) -> Optional[dict]:
        """Make a GET request to the BioPortal API with retry logic."""
        url = f"{self.endpoint.rstrip('/')}/{path.lstrip('/')}"

        @retry(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=1, max=10),
            reraise=True,
        )
        def _request():
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                if response.status_code == 404:
                    return None
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException:
                raise

        try:
            return _request()
        except Exception:
            return None

    def _sort_by_specificity(self, terms: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Sort terms by specificity (more specific terms first).

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

    def to_term_result(
        self,
        term_data: dict[str, Any],
        include_hierarchy: bool = True,
    ) -> Optional[OntologyTermResult]:
        """Convert BioPortal API response to OntologyTermResult model.

        Args:
            term_data: Raw API response data
            include_hierarchy: Whether to fetch hierarchy info

        Returns:
            Parsed OntologyTermResult or None if invalid
        """
        try:
            curie = term_data.get("ontologies", [{}])[0].get("acronym", "")
            term_id = term_data.get("id", "")

            if not curie or not term_id:
                return None

            prefix = curie

            hierarchy_info = None
            if include_hierarchy:
                hierarchy_info = self._build_hierarchy_info(term_data, prefix)

            return OntologyTermResult(
                curie=term_data.get("prefLabel", term_id),
                prefix=prefix,
                label=term_data.get("prefLabel", term_data.get("label", term_id)),
                definition=(
                    term_data.get("definition", [None])[0]
                    if term_data.get("definition")
                    else None
                ),
                synonyms=term_data.get("synonym", []),
                source=OntologySource.BIOPORTAL,
                ontology=prefix.lower(),
                hierarchy=hierarchy_info,
                metadata={
                    "id": term_id,
                    "url": term_data.get("links", {}).get("self", ""),
                    "obsolete": term_data.get("obsolete", False),
                },
            )
        except (KeyError, TypeError):
            return None

    def _build_hierarchy_info(
        self,
        term_data: dict[str, Any],
        ontology: str,
    ) -> Optional[HierarchyInfo]:
        """Build HierarchyInfo from BioPortal term data."""
        curie = term_data.get("id", "")
        if not curie:
            return None

        ancestors = term_data.get("ancestors", [])
        if isinstance(ancestors, list):
            ancestors = [a.get("id", "") for a in ancestors if isinstance(a, dict)]

        bfo_class = self._detect_bfo_class(term_data, ancestors)

        return HierarchyInfo(
            curie=curie,
            label=term_data.get("prefLabel", curie),
            ancestors=ancestors,
            bfo_class=bfo_class,
            depth=len(ancestors),
        )

    def _detect_bfo_class(
        self,
        term_data: dict[str, Any],
        ancestors: list[str],
    ) -> Optional[str]:
        """Detect BFO class from term data and ancestors."""
        for ancestor in ancestors:
            if "BFO" in ancestor:
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
            Preferred ontology acronym or None
        """
        if not candidates:
            return None

        ontology_counts: dict[str, int] = {}
        for term in candidates:
            ont = term.get("ontologies", [{}])[0].get("acronym", "unknown")
            if ont:
                ontology_counts[ont] = ontology_counts.get(ont, 0) + 1

        if ontology_counts:
            max_count = max(ontology_counts.values())
            for k, v in ontology_counts.items():
                if v == max_count:
                    return k

        return None


def get_bioportal_client(
    api_key: Optional[str] = None, timeout: int = 30
) -> BioPortalClient:
    """Create and return a BioPortalClient instance."""
    return BioPortalClient(api_key=api_key, timeout=timeout)


def search_bioportal(
    query: str,
    preferred_ontology: Optional[str] = None,
    limit: int = 10,
    timeout: int = 30,
    api_key: Optional[str] = None,
    search_synonyms: bool = True,
) -> tuple[list[OntologyTermResult], Optional[str]]:
    """Search BioPortal and return results.

    Args:
        query: Search query
        preferred_ontology: Optional preferred ontology acronym
        limit: Maximum results
        timeout: Request timeout
        api_key: BioPortal API key (optional, reads from BIOPORTAL_API_KEY)
        search_synonyms: Whether to search in synonyms

    Returns:
        Tuple of (results, suggested_ontology)
    """
    client = get_bioportal_client(api_key=api_key, timeout=timeout)

    search_ontologies = [preferred_ontology] if preferred_ontology else []

    results: list[OntologyTermResult] = []
    ontologies_to_search = search_ontologies if search_ontologies else [None]

    for ontology in ontologies_to_search:
        terms = client.search(
            query,
            ontologies=[ontology] if ontology else None,
            limit=limit,
            search_synonyms=search_synonyms,
        )
        for term_data in terms:
            result = client.to_term_result(term_data)
            if result:
                results.append(result)
        if results:
            break

    if not results and search_ontologies:
        return [], preferred_ontology

    suggested = None
    if not results:
        terms = client.search(query, limit=limit * 2, search_synonyms=search_synonyms)
        suggested = client.get_preferred_ontology(query, terms)

    return results, suggested
