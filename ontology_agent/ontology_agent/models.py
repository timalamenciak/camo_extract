"""Pydantic models for ontology search input and output.

These models define the contract between the agent and callers,
ensuring type safety and validation.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field


class OntologySource(Enum):
    """Supported ontology repositories."""

    OLS = "ols"
    BIOPORTAL = "bioportal"


class HierarchyInfo(BaseModel):
    """Information about a term's position in the ontology hierarchy."""

    curie: str = Field(description="The term's CURIE")
    label: str = Field(description="The term's label")
    parents: list[str] = Field(default_factory=list, description="Parent term CURIEs")
    ancestors: list[str] = Field(
        default_factory=list, description="All ancestor CURIEs"
    )
    bfo_class: Optional[str] = Field(
        default=None, description="Highest-level BFO class if known"
    )
    depth: int = Field(default=0, description="Distance from root")


class OntologyTermResult(BaseModel):
    """A found ontology term."""

    model_config = ConfigDict(protected_namespaces=())

    curie: str = Field(description="Full CURIE (e.g., ENVO:00001001)")
    prefix: str = Field(description="Ontology prefix (e.g., ENVO)")
    label: str = Field(description="Human-readable label")
    definition: Optional[str] = Field(default=None, description="Term definition")
    synonyms: list[str] = Field(default_factory=list, description="Known synonyms")
    source: OntologySource = Field(description="Source repository")
    ontology: str = Field(description="Ontology name")
    hierarchy: Optional[HierarchyInfo] = Field(
        default=None, description="Hierarchy information"
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )
    is_preferred: bool = Field(
        default=False, description="Whether this is the preferred/preferred term"
    )


class TermSuggestion(BaseModel):
    """A suggested new term when no match is found."""

    model_config = ConfigDict(protected_namespaces=())

    term: str = Field(description="Suggested term label")
    ontology: str = Field(description="Recommended ontology (e.g., ENVO, BFO, PATO)")
    bfo_class: Optional[str] = Field(
        default=None, description="BFO hierarchy position (CURIE)"
    )
    bfo_label: Optional[str] = Field(
        default=None, description="Human-readable BFO class name"
    )
    definition: Optional[str] = Field(
        default=None, description="Proposed definition for the term"
    )
    justification: str = Field(description="Rationale for this suggestion")
    score: float = Field(
        ge=0.0, le=1.0, description="Confidence score for this suggestion"
    )


class SearchStatus(Enum):
    """Status of a search operation."""

    FOUND = "found"
    NO_MATCH = "no_match"
    PARTIAL = "partial"


class SearchResult(BaseModel):
    """Search result, either a found term or a suggestion."""

    found: bool = Field(description="Whether an exact/appropriate match was found")
    term: Optional[OntologyTermResult] = Field(
        default=None, description="Found term if available"
    )
    suggestions: list[TermSuggestion] = Field(
        default_factory=list, description="Suggested terms if no match"
    )
    query: str = Field(description="Original search query")
    searched_ontologies: list[str] = Field(
        default_factory=list, description="Ontologies that were searched"
    )
    source: Optional[OntologySource] = Field(default=None, description="Source used")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    search_id: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class SearchResponse(BaseModel):
    """Final search response with metadata."""

    status: SearchStatus = Field(description="Overall search status")
    results: list[SearchResult] = Field(
        default_factory=list, description="Search results"
    )
    query: str = Field(description="Original search query")
    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Search parameters"
    )
    matches_found: int = Field(default=0, description="Number of exact matches found")
    suggestions_generated: int = Field(default=0, description="Number of suggestions")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    elapsed_ms: Optional[float] = Field(
        default=None, description="Search duration in milliseconds"
    )


class OntologyQuery(BaseModel):
    """Query input from the caller."""

    query: str = Field(min_length=1, description="Text query to search for")
    preferred_ontology: Optional[str] = Field(
        default=None, description="Preferred ontology (e.g., ENVO, BFO)"
    )
    ontologies: list[str] = Field(
        default_factory=list, description="Specific ontologies to search"
    )
    include_suggestions: bool = Field(
        default=True, description="Generate term suggestions if no match"
    )
    include_hierarchy: bool = Field(
        default=True, description="Include hierarchy information"
    )
    limit: int = Field(default=10, ge=1, le=50, description="Maximum results to return")
    strict: bool = Field(default=False, description="Strict matching (no fuzzy search)")


class SearchParameters(BaseModel):
    """Configuration for a search operation."""

    model_config = ConfigDict(protected_namespaces=())

    api_timeout: int = Field(
        default=30, ge=5, le=120, description="API timeout in seconds"
    )
    retry_attempts: int = Field(default=3, ge=1, le=5, description="API retry attempts")
    ols_endpoint: str = Field(
        default="https://www.ebi.ac.uk/ols4/api", description="OLS API endpoint"
    )
    bioportal_endpoint: str = Field(
        default="https://data.bioontology.org",
        description="BioPortal API endpoint",
    )
    bioportal_api_key: Optional[str] = Field(
        default=None, description="BioPortal API key (optional)"
    )
    fallback_to_suggestions: bool = Field(
        default=True, description="Fall back to suggestions when no match"
    )
