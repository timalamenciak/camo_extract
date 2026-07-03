"""Tests for main agent service."""

from ontology_agent.models import SearchStatus
from ontology_agent.services import OntologyAgent, search


def test_agent_initialization():
    """Test agent initialization."""
    agent = OntologyAgent()

    assert agent is not None
    assert agent.parameters is not None


def test_search_method():
    """Test search method exists."""
    agent = OntologyAgent()

    result = agent.search("test")

    assert result is not None
    assert hasattr(result, "status")
    assert hasattr(result, "results")


def test_find_term_by_curie():
    """Test term lookup by CURIE."""
    agent = OntologyAgent()

    result = agent.find_term_by_curie("ENVO:00001001")

    # Should return None or SearchResult (depending on API availability)
    assert result is None or hasattr(result, "found")


def test_search_convenience_function():
    """Test search convenience function."""
    result = search("test term")

    assert result is not None
    assert hasattr(result, "status")
    assert hasattr(result, "query")
    assert result.query == "test term"


def test_result_status_values():
    """Test status enum values."""
    assert SearchStatus.FOUND.value == "found"
    assert SearchStatus.NO_MATCH.value == "no_match"
    assert SearchStatus.PARTIAL.value == "partial"
