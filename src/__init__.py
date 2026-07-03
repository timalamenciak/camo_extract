"""Causal graph extractor from PDF scientific articles.

This package provides tools for extracting causal graphs from PDF
scientific articles using LLMs and grounding them in ontologies.
"""

__version__ = "0.2.0"
__author__ = "Tim Alamenciak"

from .chunker import Chunker
from .config import Config, load_config
from .consolidator import Consolidator
from .graph_extractor import GraphExtractor
from .ontology_grounder import OntologyGrounder
from .pdf_processor import PDFProcessor
from .risc_reader import RISReader
from .schema_validation import normalize_graph, validate_graph
from .validator import Validator

__all__ = [
    "PDFProcessor",
    "Chunker",
    "GraphExtractor",
    "RISReader",
    "Validator",
    "Consolidator",
    "Config",
    "load_config",
    "OntologyGrounder",
    "normalize_graph",
    "validate_graph",
]
