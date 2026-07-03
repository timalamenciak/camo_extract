"""MainOntologyAgent service coordinating all components.

This module provides the primary interface for ontology search and term suggestion.
"""

from __future__ import annotations

import time
from typing import Optional

from ..config import AgentConfig, load_config
from ..models import (
    OntologyQuery,
    OntologyTermResult,
    SearchParameters,
    SearchResponse,
    SearchResult,
    SearchStatus,
)
from .bioportal import search_bioportal
from .custom_ontology import search_custom_ontology
from .generator import generate_suggestions
from .ols import get_ols_client, search_ols

HAS_HTTPX = False
try:
    import importlib.util

    if importlib.util.find_spec("httpx"):
        HAS_HTTPX = True
except ImportError:
    pass


class OntologyAgent:
    """Main agent service for ontology lookup and term suggestion."""

    def __init__(
        self,
        parameters: Optional[SearchParameters] = None,
        config: Optional[AgentConfig] = None,
        config_path: Optional[str] = None,
    ):
        if config is None:
            config = load_config(config_path)

        if parameters is None:
            parameters = SearchParameters(
                bioportal_endpoint=config.bioportal_endpoint,
                ols_endpoint=config.ols_endpoint,
                bioportal_api_key=config.bioportal_api_key,
                fallback_to_suggestions=config.fallback_to_suggestions,
            )

        self.parameters = parameters
        self.config = config

    def search(
        self,
        query: str,
        preferred_ontology: Optional[str] = None,
        ontologies: Optional[list[str]] = None,
        include_suggestions: bool = True,
        include_hierarchy: bool = True,
        strict: bool = False,
        limit: int = 10,
    ) -> SearchResponse:
        """Search ontology databases and generate suggestions.

        Args:
            query: Text query to search for
            preferred_ontology: Preferred ontology (e.g., "ENVO")
            ontologies: Specific ontologies to search
            include_suggestions: Generate term suggestions if no match
            include_hierarchy: Include hierarchy information
            strict: Strict matching (no fuzzy search)
            limit: Maximum results to return

        Returns:
            SearchResponse with results and/or suggestions
        """
        start_time = time.time()

        query_obj = OntologyQuery(
            query=query,
            preferred_ontology=preferred_ontology,
            ontologies=ontologies or [],
            include_suggestions=include_suggestions,
            include_hierarchy=include_hierarchy,
            limit=limit,
            strict=strict,
        )

        searched_ontologies = query_obj.ontologies
        if query_obj.preferred_ontology:
            searched_ontologies = [query_obj.preferred_ontology] + searched_ontologies

        custom_ontos = (
            [o.name for o in self.config.custom_ontologies]
            if self.config and self.config.custom_ontologies
            else []
        )

        results = self._execute_search(
            query_obj, include_hierarchy, strict, custom_ontos
        )

        elapsed = (time.time() - start_time) * 1000

        matches_found = sum(1 for r in results if r.found)
        suggestions_generated = sum(len(r.suggestions) for r in results)

        status = SearchStatus.FOUND if matches_found > 0 else SearchStatus.NO_MATCH

        if not results and include_suggestions:
            all_searched = searched_ontologies + custom_ontos
            suggestions, _ = generate_suggestions(
                query_obj.query,
                all_searched,
                query_obj.preferred_ontology,
                limit,
            )
            if suggestions:
                results.append(
                    SearchResult(
                        found=False,
                        term=None,
                        suggestions=suggestions,
                        query=query_obj.query,
                        searched_ontologies=all_searched,
                    )
                )
                status = SearchStatus.PARTIAL

        return SearchResponse(
            status=status,
            results=results,
            query=query_obj.query,
            parameters=query_obj.model_dump(),
            matches_found=matches_found,
            suggestions_generated=suggestions_generated,
            elapsed_ms=round(elapsed, 2),
        )

    def _execute_search(
        self,
        query_obj: OntologyQuery,
        include_hierarchy: bool,
        strict: bool,
        custom_ontologies: list[str],
    ) -> list[SearchResult]:
        """Execute the actual search across OLS, BioPortal, and custom ontologies."""
        results = []

        all_results: list[OntologyTermResult] = []

        ols_results, _ = search_ols(
            query=query_obj.query,
            preferred_ontology=query_obj.preferred_ontology,
            limit=query_obj.limit,
            timeout=self.parameters.api_timeout,
            search_synonyms=True,
            endpoint=self.parameters.ols_endpoint,
        )

        all_results.extend(ols_results)

        if not ols_results and query_obj.ontologies:
            bp_results, _ = search_bioportal(
                query=query_obj.query,
                preferred_ontology=query_obj.preferred_ontology,
                limit=query_obj.limit,
                timeout=self.parameters.api_timeout,
                api_key=self.parameters.bioportal_api_key,
                search_synonyms=True,
                endpoint=self.parameters.bioportal_endpoint,
            )

            all_results.extend(bp_results)

        custom_results = []
        for custom_onto in self.config.custom_ontologies or []:
            if custom_onto.name in custom_ontologies:
                custom_results.extend(
                    search_custom_ontology(
                        query=query_obj.query,
                        name=custom_onto.name,
                        url=custom_onto.url,
                        prefix=custom_onto.prefix,
                        limit=query_obj.limit,
                        timeout=self.config.llm.timeout if self.config.llm else 30,
                    )
                )

        all_results.extend(custom_results)

        ranked_results = self._sort_and_rank_results(all_results, query_obj.query)

        if self.config and self.config.llm and HAS_HTTPX:
            ranked_results = self._assess_term_quality_with_llm(
                ranked_results, query_obj.query
            )

        for result in ranked_results[: query_obj.limit]:
            results.append(
                SearchResult(
                    found=True,
                    term=result,
                    suggestions=[],
                    query=query_obj.query,
                    searched_ontologies=query_obj.ontologies,
                )
            )

        if not results and query_obj.include_suggestions:
            suggestions, _ = generate_suggestions(
                query_obj.query,
                query_obj.ontologies,
                query_obj.preferred_ontology,
                query_obj.limit,
            )
            if suggestions:
                results.append(
                    SearchResult(
                        found=False,
                        term=None,
                        suggestions=suggestions,
                        query=query_obj.query,
                        searched_ontologies=query_obj.ontologies,
                    )
                )

        return results

    def _sort_and_rank_results(
        self, results: list[OntologyTermResult], query: str
    ) -> list[OntologyTermResult]:
        """Sort and rank results by quality indicators.

        Applies multiple scoring factors to identify the best term:
        - Specificity (more ancestors = more specific)
        - Ontology reputation (preferred ontologies score higher)
        - Term length (shorter labels often better for common terms)
        - Match quality with query

        Args:
            results: List of term results
            query: Original search query

        Returns:
            Ranked list (best term first, marked as preferred)
        """
        preferred_ontologies = {
            "pato",
            "go",
            "envo",
            "elmo",
            "chebi",
            "bfo",
            "cl",
            "fao",
        }

        def quality_score(term: OntologyTermResult) -> float:
            score = 0.0

            if term.hierarchy and term.hierarchy.ancestors:
                score += len(term.hierarchy.ancestors) * 0.1

            ontology_lower = term.ontology.lower()
            if ontology_lower in preferred_ontologies:
                score += 0.3

            label = term.label.lower()
            query_lower = query.lower()
            if label == query_lower:
                score += 0.5
            elif query_lower in label:
                score += 0.3

            if len(label.split()) <= 3:
                score += 0.1

            if term.metadata.get("is_defining_ontology", False):
                score += 0.2

            return score

        ranked = sorted(results, key=quality_score, reverse=True)

        if ranked:
            ranked[0].is_preferred = True

        return ranked

    def _assess_term_quality_with_llm(
        self, results: list[OntologyTermResult], query: str
    ) -> list[OntologyTermResult]:
        """Use LLM to assess term quality and relevance.

        Sends a lightweight request to LLM to rank terms by quality.
        Falls back to rule-based ranking if LLM unavailable.

        Args:
            results: Ranked term results
            query: Original search query

        Returns:
            Results with potentially adjusted rankings
        """
        if len(results) < 2:
            return results

        if not self.config or not self.config.llm:
            return results

        try:
            prompt = self._build_term_ranking_prompt(query, results)

            if not HAS_HTTPX:
                return results

            response = self._call_llm(prompt, self.config.llm)

            if response:
                new_order = self._parse_llm_ranking(response, results)
                if new_order:
                    return new_order

        except Exception:
            pass

        return results

    def _build_term_ranking_prompt(
        self, query: str, results: list[OntologyTermResult]
    ) -> str:
        """Build LLM prompt for term ranking."""
        terms_info = []
        for i, term in enumerate(results, 1):
            term_info = (
                f"{i}. {term.label} (CURIE: {term.curie}, Ontology: {term.ontology})"
            )
            if term.definition:
                term_info += f"\n   Definition: {term.definition}"
            terms_info.append(term_info)

        definition_text = (
            f"Definition: {results[0].definition}"
            if results[0].definition
            else "No definition available"
        )

        prompt = f"""Rank the following ontology terms by quality and relevance to the query "{query}".

Best terms typically:
- Have clear, precise definitions
- Are specific but not overly narrow
- Come from reputable ontologies (PATO, GO, ENVO, CHEBI, BFO)
- Match the query semantics well

Query: "{query}"
{definition_text}

Terms to rank:
{chr(10).join(terms_info)}

Output only the numbered ranking (e.g., "2, 1, 3"):"""

        return prompt

    def _call_llm(self, prompt: str, llm_config) -> Optional[str]:
        """Call LLM endpoint with ranking prompt."""
        try:
            import httpx

            headers = {"Content-Type": "application/json"}

            if llm_config.api_key:
                headers["Authorization"] = f"Bearer {llm_config.api_key}"

            messages = [{"role": "user", "content": prompt}]

            body = {"messages": messages}
            if llm_config.model:
                body["model"] = llm_config.model

            with httpx.Client(timeout=llm_config.timeout) as client:
                response = client.post(
                    llm_config.endpoint.rstrip("/") + "/chat/completions",
                    json=body,
                    headers=headers,
                )
                response.raise_for_status()
                result = response.json()
                return (
                    result.get("choices", [{}])[0].get("message", {}).get("content", "")
                )

        except Exception:
            return None

    def _parse_llm_ranking(
        self, response: str, original_results: list[OntologyTermResult]
    ) -> Optional[list[OntologyTermResult]]:
        """Parse LLM ranking response and reorder results."""
        import re

        match = re.search(r"(\d+(?:,\s*\d+)*)", response)
        if not match:
            return None

        try:
            ranked_indices = [int(x.strip()) - 1 for x in match.group(1).split(",")]

            if not all(0 <= i < len(original_results) for i in ranked_indices):
                return None

            new_order = [original_results[i] for i in ranked_indices]

            for i, term in enumerate(new_order):
                term.is_preferred = i == 0

            return new_order

        except Exception:
            return None

    def find_term_by_curie(
        self,
        curie: str,
        preferred_ontology: Optional[str] = None,
    ) -> Optional[SearchResult]:
        """Look up a term by its CURIE.

        Args:
            curie: Full CURIE (e.g., "ENVO:00001001")
            preferred_ontology: Optional preferred ontology

        Returns:
            SearchResult with term details or None
        """
        prefix = curie.split(":")[0] if ":" in curie else preferred_ontology

        if prefix:
            term_id = curie.split(":")[1] if ":" in curie else curie

            # Check custom ontologies first
            for custom_onto in self.config.custom_ontologies or []:
                if custom_onto.prefix == prefix:
                    from .custom_ontology import get_custom_client

                    client = get_custom_client(
                        url=custom_onto.url,
                        name=custom_onto.name,
                        prefix=custom_onto.prefix,
                        timeout=self.config.llm.timeout if self.config.llm else 30,
                    )
                    if not client._term_cache:
                        client._build_cache()
                    term_result = client.get_term(term_id)
                    if term_result:
                        return SearchResult(
                            found=True,
                            term=term_result,
                            suggestions=[],
                            query=curie,
                            searched_ontologies=[prefix],
                        )

        client_ols = get_ols_client(
            timeout=self.parameters.api_timeout, endpoint=self.parameters.ols_endpoint
        )

        if prefix:
            term_id = curie.split(":")[1] if ":" in curie else curie
            term_data = client_ols.get_term(prefix, term_id)

            if term_data:
                term_result = client_ols.to_term_result(term_data)
                if term_result:
                    return SearchResult(
                        found=True,
                        term=term_result,
                        suggestions=[],
                        query=curie,
                        searched_ontologies=[prefix],
                    )

        return None


def get_ontology_client(
    source: Optional[str] = None,
    api_key: Optional[str] = None,
) -> OntologyAgent:
    """Factory function to create anOntologyAgent instance.

    Args:
        source: Preferred ontology source ("ols" or "bioportal")
        api_key: BioPortal API key if needed

    Returns:
        Configured OntologyAgent
    """
    params = SearchParameters()

    if source == "bioportal" and api_key:
        params.bioportal_api_key = api_key

    return OntologyAgent(parameters=params)


def search(
    query: str,
    preferred_ontology: Optional[str] = None,
    ontologies: Optional[list[str]] = None,
    include_suggestions: bool = True,
    include_hierarchy: bool = True,
    limit: int = 10,
) -> SearchResponse:
    """Convenience function for quick ontology searches.

    Args:
        query: Text query
        preferred_ontology: Preferred ontology
        ontologies: Specific ontologies to search
        include_suggestions: Generate suggestions if no match
        include_hierarchy: Include hierarchy info
        limit: Maximum results

    Returns:
        SearchResponse
    """
    agent = OntologyAgent()
    return agent.search(
        query=query,
        preferred_ontology=preferred_ontology,
        ontologies=ontologies,
        include_suggestions=include_suggestions,
        include_hierarchy=include_hierarchy,
        limit=limit,
    )
