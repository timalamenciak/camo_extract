"""Main entry point for causal graph extraction."""

import json
import yaml  # type: ignore[import-untyped]
from pathlib import Path
from typing import Optional

from .risc_reader import RISReader, ArticleMetadata
from .pdf_processor import PDFProcessor
from .chunker import Chunker
from .graph_extractor import GraphExtractor
from .consolidator import Consolidator
from .config import Config, load_config


def process_folder(
    input_dir: str,
    output_dir: str,
    config: Optional[Config] = None,
    config_path: Optional[str] = None,
    test_mode: bool = False,
    max_articles: int = 5,
) -> None:
    """Process all PDFs in a folder.

    Args:
        input_dir: Directory containing PDFs and RIS file
        output_dir: Directory for output files
        config: Config instance (optional)
        config_path: Path to config file (optional)
        test_mode: If True, only process first N articles (default: 5)
        max_articles: Number of articles to process in test mode
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)

    if config is None:
        config = load_config(config_path)

    # Find RIS file
    ris_files = list(input_path.glob("*.ris"))
    if not ris_files:
        print("No RIS file found in input directory")
        return
    ris_file = ris_files[0]

    # Read RIS metadata
    ris_reader = RISReader()
    articles = ris_reader.read_file(str(ris_file))

    # Handle test mode
    if test_mode:
        articles = articles[:max_articles]
        print(f"TEST MODE: Processing first {len(articles)} articles")

    # Find PDF files
    pdf_files = list(input_path.glob("*.pdf"))

    # Load existing partial results for resumability
    existing_graphs = _load_partial_results(output_path)
    processed_dois = {
        g.get("metadata", {}).get("source_doi", "") for g in existing_graphs
    }

    print(f"Found {len(existing_graphs)} previously processed graphs")

    # Process each PDF
    all_graphs = existing_graphs.copy()
    for article in articles:
        # Skip if already processed (resumability)
        if article.doi and article.doi in processed_dois:
            print(f"Skipping already processed: {article.title}")
            continue

        # Find corresponding PDF
        pdf_file = _find_pdf_for_article(article, pdf_files)
        if not pdf_file:
            print(f"No PDF found for article: {article.title or 'unknown'}")
            continue

        print(f"\nProcessing: {article.title}")

        # Extract graph
        graph = extract_graph_from_pdf(
            pdf_path=str(pdf_file),
            article_metadata=article,
            config=config,
        )

        if graph:
            # Add DOI to metadata for resumability
            if article.doi:
                graph.setdefault("metadata", {})["source_doi"] = article.doi
            if article.title:
                graph.setdefault("metadata", {})["source_title"] = article.title

            all_graphs.append(graph)

            # Save individual graph for resumability
            _save_intermediate_result(graph, article, output_path)

            # Save partial consolidation
            consolidator = Consolidator(
                merge_duplicated_nodes=config.output.merge_duplicated_nodes,
                deduplicate_edges=True,
            )
            partial_consolidated = consolidator.consolidate(all_graphs)
            _save_outputs(partial_consolidated, output_path)

    # Final consolidation and save
    print("\nFinal consolidation...")
    consolidator = Consolidator(
        merge_duplicated_nodes=config.output.merge_duplicated_nodes,
        deduplicate_edges=True,
    )
    consolidated = consolidator.consolidate(all_graphs)

    # Save final outputs
    _save_outputs(consolidated, output_path)


def extract_graph_from_pdf(
    pdf_path: str,
    article_metadata: Optional[ArticleMetadata] = None,
    config: Optional[Config] = None,
) -> Optional[dict]:
    """Extract graph from a single PDF.

    Args:
        pdf_path: Path to PDF file
        article_metadata: Article metadata (optional)
        config: Config instance (optional)

    Returns:
        Graph dict or None if failed
    """
    if config is None:
        config = load_config()

    # Create temp output directory for intermediate files
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir)

        try:
            # Convert PDF to Markdown
            processor = PDFProcessor(
                ollama_endpoint=config.llm.endpoint,
                ollama_model=config.llm.model,
                use_llm_assist=True,
            )
            markdown = processor.convert_to_markdown(
                pdf_path, output_dir=str(output_path / "tmp_md")
            )

            # Chunk text
            chunker = Chunker(
                max_chunk_size=config.chunking.max_characters_per_chunk,
                overlap_size=config.chunking.max_characters_per_chunk // 10,
            )
            chunks = chunker.chunk_text(markdown)

            # Extract graph for each chunk
            extractor = GraphExtractor(
                llm_endpoint=config.llm.endpoint,
                llm_model=config.llm.model,
                api_key=config.llm.api_key,
            )

            all_graphs = []
            article_metadata_dict = {}
            if article_metadata:
                article_metadata_dict = {
                    "title": article_metadata.title,
                    "year": article_metadata.year,
                    "doi": article_metadata.doi,
                    "authors": article_metadata.authors,
                }

            for chunk in chunks:
                graph = extractor.extract(chunk.text, article_metadata_dict)
                all_graphs.append(graph)

            # Consolidate
            consolidator = Consolidator()
            return consolidator.consolidate(all_graphs)

        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return None


def _find_pdf_for_article(
    article: ArticleMetadata, pdf_files: list[Path]
) -> Optional[Path]:
    """Find PDF file matching article."""
    if not article.doi:
        return None

    # Try to match by DOI
    doi = article.doi.replace("/", "_")
    for pdf in pdf_files:
        if doi in pdf.stem:
            return pdf

    # Fall back to first PDF
    return pdf_files[0] if pdf_files else None


def _load_partial_results(output_path: Path) -> list[dict]:
    """Load existing partial results for resumability.

    Args:
        output_path: Output directory

    Returns:
        List of already-processed graph dicts
    """
    partial_dir = output_path / "partial"
    if not partial_dir.exists():
        return []

    graphs = []
    for json_file in partial_dir.glob("*.json"):
        try:
            with open(json_file, "r") as f:
                graph = json.load(f)
                graphs.append(graph)
        except Exception as e:
            print(f"Warning: Could not load {json_file}: {e}")

    return graphs


def _save_intermediate_result(
    graph: dict, article: ArticleMetadata, output_path: Path
) -> None:
    """Save individual graph for resumability.

    Args:
        graph: Graph dict to save
        article: Article metadata
        output_path: Output directory
    """
    partial_dir = output_path / "partial"
    partial_dir.mkdir(parents=True, exist_ok=True)

    # Use DOI or title as filename
    if article.doi:
        filename = f"graph_{article.doi.replace('/', '_')}.json"
    elif article.title:
        # Sanitize title for filename
        safe_title = "".join(c for c in article.title if c.isalnum() or c in " -_")[:50]
        filename = f"graph_{safe_title}.json"
    else:
        filename = f"graph_{len(list(partial_dir.glob('*.json'))):03d}.json"

    filepath = partial_dir / filename
    with open(filepath, "w") as f:
        json.dump(graph, f, indent=2)
    print(f"  Saved partial result: {filepath.name}")


def _save_outputs(graph: dict, output_path: Path) -> None:
    """Save graph to output files.

    Args:
        graph: Graph dict to save
        output_path: Output directory
    """
    # JSON output
    json_path = output_path / "causal_graph.json"
    with open(json_path, "w") as f:
        json.dump(graph, f, indent=2)
    print(f"Saved JSON to: {json_path}")

    # YAML output
    yaml_path = output_path / "causal_graph.yaml"
    with open(yaml_path, "w") as f:
        yaml.dump(graph, f, default_flow_style=False, sort_keys=False)
    print(f"Saved YAML to: {yaml_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract causal graph from PDF scientific articles"
    )
    parser.add_argument(
        "input_dir",
        help="Directory containing PDFs and RIS file",
    )
    parser.add_argument(
        "output_dir",
        help="Directory for output files",
    )
    parser.add_argument(
        "--config",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="Process only first 5 articles (test mode)",
    )
    parser.add_argument(
        "--max-articles",
        type=int,
        default=5,
        help="Number of articles to process in test mode (default: 5)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from partial results if exists",
    )

    args = parser.parse_args()

    process_folder(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        config_path=args.config,
        test_mode=args.test_mode,
        max_articles=args.max_articles,
    )


if __name__ == "__main__":
    main()
