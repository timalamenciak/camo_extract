"""Causal graph extractor from PDF scientific articles.

This package provides tools for extracting causal graphs from PDF
scientific articles using LLMs and grounding them in ontologies.
"""

__version__ = "0.1.0"
__author__ = "Tim Alamenciak"

from .pdf_processor import PDFProcessor
from .chunker import Chunker
from .graph_extractor import GraphExtractor
from .risc_reader import RISReader
from .validator import Validator
from .consolidator import Consolidator
from .config import Config, load_config

__all__ = [
    "PDFProcessor",
    "Chunker",
    "GraphExtractor",
    "RISReader",
    "Validator",
    "Consolidator",
    "Config",
    "load_config",
]
