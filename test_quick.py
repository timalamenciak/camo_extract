"""Fast smoke tests retained for backwards compatibility."""

from pathlib import Path

from src.config import load_config
from src.risc_reader import RISReader


def test_ris_reader():
    articles = RISReader().read_file(
        str(Path(__file__).parent / "data" / "input" / "sample_articles.ris")
    )
    assert len(articles) == 5
    assert articles[0].doi


def test_config():
    config = load_config()
    assert config.llm.model
    assert "ELMO" in config.ontology.default_ontologies


def test_imports():
    from src.consolidator import Consolidator
    from src.graph_extractor import GraphExtractor
    from src.ontology_grounder import OntologyGrounder
    from src.pdf_processor import PDFProcessor
    from src.schema_validation import validate_graph

    assert all(
        (Consolidator, GraphExtractor, OntologyGrounder, PDFProcessor, validate_graph)
    )
