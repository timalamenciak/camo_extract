"""Tests for term suggestion generator."""

from ontology_agent.models import TermSuggestion
from ontology_agent.services.generator import TermGenerator, generate_suggestions


def test_entity_classification():
    """Test entity type classification."""
    generator = TermGenerator()

    # Environmental entity
    assert generator._classify_entity("temperate grassland") == "environmental"

    # Process
    assert generator._classify_entity("cell division") == "process"

    # Quality
    assert generator._classify_entity("growth rate") == "quality"

    # Material
    assert generator._classify_entity("water molecule") == "material"


def test_bfo_mapping():
    """Test BFO class mapping."""
    generator = TermGenerator()

    assert generator._map_to_bfo("environmental") == "BFO:0000004"
    assert generator._map_to_bfo("process") == "BFO:0000015"
    assert generator._map_to_bfo("quality") == "BFO:0000020"
    assert generator._map_to_bfo("material") == "BFO:0000004"


def test_suggestion_generation():
    """Test term suggestion generation."""
    generator = TermGenerator()

    suggestions = generator.generate_suggestions(
        "temperate grassland",
        ontologies_searched=["ENVO"],
        limit=3,
    )

    assert len(suggestions) >= 1
    assert isinstance(suggestions[0], TermSuggestion)
    assert suggestions[0].ontology == "ENVO"
    assert suggestions[0].bfo_class == "BFO:0000004"


def test_suggestion_with_preferred_ontology():
    """Test suggestion with preferred ontology."""
    generator = TermGenerator(preferred_ontology="BFO")

    suggestions = generator.generate_suggestions(
        "cell process",
        ontologies_searched=["GO"],
        limit=3,
    )

    assert len(suggestions) >= 1
    assert suggestions[0].ontology == "BFO"


def test_generate_suggestions_convenience():
    """Test convenience function."""
    suggestions, bfo_class = generate_suggestions(
        "temperate grassland",
        ontologies_searched=["ENVO"],
        limit=3,
    )

    assert len(suggestions) >= 1
    assert bfo_class == "BFO:0000004"


def test_hierarchy_path():
    """Test hierarchy path estimation."""
    generator = TermGenerator()

    path = generator.estimate_bfo_hierarchy_path("BFO:0000020")

    assert len(path) >= 2
    assert path[0][0] == "BFO:0000001"
    assert path[-1][0] == "BFO:0000020"
