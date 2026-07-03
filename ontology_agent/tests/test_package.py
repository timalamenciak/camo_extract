"""Test package initialization."""


def test_version():
    """Test that package has a version."""
    import ontology_agent

    assert hasattr(ontology_agent, "__version__")
    assert ontology_agent.__version__ == "0.1.0"


def test_exports():
    """Test that core classes are exported."""
    from ontology_agent import (
        HierarchyInfo,
        OntologyAgent,
        OntologyQuery,
        OntologyTermResult,
        SearchParameters,
        SearchResponse,
        SearchResult,
        TermSuggestion,
    )

    assert OntologyAgent is not None
    assert OntologyQuery is not None
    assert SearchParameters is not None
    assert OntologyTermResult is not None
    assert HierarchyInfo is not None
    assert TermSuggestion is not None
    assert SearchResult is not None
    assert SearchResponse is not None
