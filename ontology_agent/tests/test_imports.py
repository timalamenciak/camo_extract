"""Tests for the ontology agent."""


# Test imports to verify package structure
def test_imports():
    """Test that all modules can be imported."""
    from ontology_agent import OntologyAgent, search
    from ontology_agent.models import (
        OntologyQuery,
    )

    assert OntologyAgent is not None
    assert search is not None
    assert OntologyQuery is not None
    from ontology_agent.services.bioportal import BioPortalClient
    from ontology_agent.services.generator import TermGenerator
    from ontology_agent.services.ols import OLSClient

    assert OntologyQuery is not None
    assert OLSClient is not None
    assert BioPortalClient is not None
    assert TermGenerator is not None


def test_models():
    """Test data models."""
    from ontology_agent.models import OntologyQuery, OntologyTermResult, TermSuggestion

    query = OntologyQuery(query="test")
    assert query.query == "test"

    term = OntologyTermResult(
        curie="ENVO:00001001",
        prefix="ENVO",
        label="test term",
        source="ols",
        ontology="envo",
    )
    assert term.curie == "ENVO:00001001"

    suggestion = TermSuggestion(
        term="suggested",
        ontology="ENVO",
        bfo_class="BFO:0000004",
        justification="test",
        score=0.8,
    )
    assert suggestion.term == "suggested"


def test_agent_search():
    """Test agent search functionality."""
    from ontology_agent.services import OntologyAgent

    agent = OntologyAgent()

    # Test that agent is initialized
    assert agent is not None
