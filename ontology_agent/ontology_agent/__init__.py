"""Standalone ontology lookup agent with term suggestion capabilities.

This package provides services for:
- Searching ontology terms via OLS and BioPortal APIs
- Generating term suggestions when no match is found
- Mapping terms to BFO hierarchy positions
- Returning structured JSON results

Usage:
    from ontology_agent import OntologyAgent

    agent = OntologyAgent()
    result = agent.search("temperate grassland", preferred_ontology="ENVO")
"""

__version__ = "0.1.0"

from .config import AgentConfig, CustomOntology, LLMConfig, load_config, save_config
from .models import (
    HierarchyInfo,
    OntologyQuery,
    OntologyTermResult,
    SearchParameters,
    SearchResponse,
    SearchResult,
    TermSuggestion,
)
from .services import OntologyAgent, get_ontology_client, search

__all__ = [
    "OntologyQuery",
    "SearchParameters",
    "OntologyTermResult",
    "HierarchyInfo",
    "TermSuggestion",
    "SearchResult",
    "SearchResponse",
    "OntologyAgent",
    "get_ontology_client",
    "search",
    "AgentConfig",
    "CustomOntology",
    "LLMConfig",
    "load_config",
    "save_config",
    "__version__",
]
