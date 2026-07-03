#!/usr/bin/env python3
"""Quick test script for causal graph extraction."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from risc_reader import RISReader
from config import load_config


def test_ris_reader():
    """Test RIS reader with sample data."""
    print("Testing RIS reader...")
    reader = RISReader()
    
    ris_path = Path(__file__).parent / "data" / "input" / "sample_articles.ris"
    articles = reader.read_file(str(ris_path))
    
    print(f"Found {len(articles)} articles:")
    for i, article in enumerate(articles, 1):
        print(f"  {i}. {article.title[:50]}... ({article.year})")
    
    print("\nTesting test mode (first 5 articles):")
    test_articles = articles[:5]
    print(f"  Processing {len(test_articles)} articles in test mode")
    
    print("✓ RIS reader test passed!")
    return articles


def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    config = load_config()
    
    print(f"LLM Model: {config.llm.model}")
    print(f"Chunk size: {config.chunking.max_characters_per_chunk} chars")
    print(f"Test mode max_articles: {config.llm.max_tokens}")
    print("✓ Configuration test passed!")
    return config


def test_imports():
    """Test all imports."""
    print("\nTesting imports...")
    from pdf_processor import PDFProcessor
    from chunker import Chunker
    from graph_extractor import GraphExtractor
    from validator import Validator
    from consolidator import Consolidator
    
    print("✓ All imports successful!")
    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("Causal Graph Extractor - Quick Test")
    print("=" * 60)
    
    try:
        test_imports()
        test_ris_reader()
        test_config()
        
        print("\nTesting resumable processing structure...")
        from src.main import _load_partial_results
        from pathlib import Path
        result = _load_partial_results(Path("test_output"))
        print(f"Partial results loader works: found {len(result)} graphs")
        
        print("\n" + "=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        return 0
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
