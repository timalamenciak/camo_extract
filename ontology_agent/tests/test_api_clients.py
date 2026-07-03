"""Tests for the ontology agent package."""

from unittest.mock import patch

from ontology_agent.models import OntologySource
from ontology_agent.services.generator import TermGenerator
from ontology_agent.services.ols import OLSClient


def test_ols_search():
    """Test OLS search with mock."""
    with patch("ontology_agent.services.ols.requests.Session") as mock_session:
        mock_session.return_value.get.return_value.status_code = 200
        mock_session.return_value.get.return_value.json.return_value = {
            "_embedded": {
                "terms": [
                    {
                        "iri": "http://purl.obolibrary.org/obo/ENVO_00001001",
                        "ontology_name": "envo",
                        "curie": "ENVO:00001001",
                        "label": "grassland",
                        "description": ["A temperate grassland"],
                        "synonym": ["temperate grassland"],
                    }
                ]
            }
        }

        client = OLSClient(timeout=5)
        results = client.search("grassland", limit=10)

        assert len(results) == 1
        assert results[0]["label"] == "grassland"


def test_ols_to_term_result():
    """Test OLS result parsing."""
    client = OLSClient(timeout=5)

    term_data = {
        "iri": "http://purl.obolibrary.org/obo/ENVO_00001001",
        "ontology_name": "envo",
        "curie": "ENVO:00001001",
        "label": "grassland",
        "description": ["A temperate grassland"],
        "synonym": ["temperate grassland"],
    }

    result = client.to_term_result(term_data)

    assert result is not None
    assert result.curie == "ENVO:00001001"
    assert result.label == "grassland"
    assert result.source == OntologySource.OLS


def test_entity_classification():
    """Test entity type classification."""
    generator = TermGenerator()

    assert generator._classify_entity("temperate grassland") == "environmental"
    assert generator._classify_entity("cell division") == "process"
    assert generator._classify_entity("growth rate") == "quality"


def test_bfo_mapping():
    """Test BFO class mapping."""
    generator = TermGenerator()

    assert generator._map_to_bfo("environmental") == "BFO:0000004"
    assert generator._map_to_bfo("process") == "BFO:0000015"
    assert generator._map_to_bfo("quality") == "BFO:0000020"
