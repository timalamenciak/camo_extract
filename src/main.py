"""Command-line orchestration for CAMO extraction."""

from __future__ import annotations

import csv
import json
import logging
import os
import re
import sys
import tempfile
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

from .chunker import Chunker
from .config import Config, load_config
from .consolidator import Consolidator
from .gap_report import GapReport
from .graph_extractor import GraphExtractor
from .ontology_grounder import GroundingDecision, OntologyGrounder, normalize_label
from .pdf_processor import PDFProcessor
from .risc_reader import ArticleMetadata, RISReader
from .schema_validation import normalize_graph, validate_graph

LOGGER = logging.getLogger("camo_extract")


def _make_unique_output_path(output_dir: str) -> Path:
    """Create output path with timestamp suffix if directory exists and has content."""
    output_path = Path(output_dir)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    unique_suffix = f"_{timestamp}_{uuid.uuid4().hex[:8]}"

    if output_path.exists() and any(output_path.iterdir()):
        new_path = output_path.parent / f"{output_path.name}{unique_suffix}"
        new_path.mkdir(parents=True, exist_ok=True)
        LOGGER.info(f"Output folder exists; created unique: {new_path}")
        return new_path

    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def process_folder(
    input_dir: str,
    output_dir: str,
    config: Optional[Config] = None,
    config_path: Optional[str] = None,
    test_mode: bool = False,
    max_articles: int = 5,
    resume: bool = False,
    extractor: Optional[GraphExtractor] = None,
    grounder: Optional[OntologyGrounder] = None,
    pdf_processor: Optional[PDFProcessor] = None,
    make_unique: bool = True,
) -> dict:
    """Process an RIS-described PDF corpus and return a processing manifest.

    If make_unique is True and output_dir exists with content, creates a timestamped
    unique folder (e.g., output_20260705_142345_a1b2c3d4). Otherwise, uses output_dir
    directly. Set resume=True to continue from existing partial results.
    """
    input_path = Path(input_dir)
    output_path = (
        _make_unique_output_path(output_dir) if make_unique else Path(output_dir)
    )
    config = config or load_config(config_path)

    ris_files = sorted(input_path.glob("*.ris"))
    if len(ris_files) != 1:
        raise ValueError(
            f"Expected exactly one RIS file in {input_path}; found {len(ris_files)}"
        )
    articles = RISReader().read_file(str(ris_files[0]))
    if test_mode:
        articles = articles[:max_articles]
    pdf_files = sorted(input_path.glob("*.pdf"))
    LOGGER.info(
        "Starting corpus: %d article(s), %d PDF(s), output=%s",
        len(articles),
        len(pdf_files),
        output_path,
    )

    existing_graphs = _load_partial_results(output_path) if resume else []
    gap_report = GapReport(
        {
            "ELMO": {"version": "2026-07-03", "url": config.ontology.elmo_url},
            "OLS": {"url": config.ontology.ols_endpoint},
            "Wikidata": {"url": config.ontology.wikidata_endpoint},
        }
    )
    if resume:
        _restore_partial_gaps(output_path, gap_report)
    processed_keys = {
        edge.get("source_document", {}).get("doi")
        for graph in existing_graphs
        for edge in graph.get("edges", [])
        if edge.get("source_document", {}).get("doi")
    }
    processed_keys.update(
        graph.get("provenance", {}).get("source_corpus") for graph in existing_graphs
    )
    manifest: dict[str, list[dict]] = {
        "processed": [],
        "skipped": [],
        "failed": [],
    }
    if resume:
        manifest = _load_processing_manifest(output_path, manifest)
    graphs = list(existing_graphs)
    _save_progress_reports(gap_report.to_dict(), manifest, output_path)

    extractor = extractor or GraphExtractor(
        llm_endpoint=config.llm.endpoint,
        llm_model=config.llm.model,
        api_key=config.llm.api_key,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
        timeout=config.llm.timeout,
        provider=config.llm.provider,
    )
    grounder = grounder or OntologyGrounder(
        config.ontology.ols_endpoint,
        config.ontology.elmo_url,
        config.ontology.wikidata_endpoint,
        config.ontology.request_timeout,
        config.ontology.suggestion_threshold,
    )

    for article_number, article in enumerate(articles, 1):
        article_key = article.doi or article.record_id or article.title or "unknown"
        LOGGER.info(
            "[%d/%d] Article: %s",
            article_number,
            len(articles),
            article.title or article_key,
        )
        if resume and (
            (article.doi and article.doi in processed_keys)
            or article.title in processed_keys
        ):
            manifest["skipped"].append(
                {"article": article_key, "reason": "already processed"}
            )
            LOGGER.info(
                "[%d/%d] Skipped: already processed",
                article_number,
                len(articles),
            )
            _save_progress_reports(gap_report.to_dict(), manifest, output_path)
            continue
        pdf_file = _find_pdf_for_article(article, pdf_files)
        if pdf_file is None:
            manifest["failed"].append(
                {"article": article_key, "error": "No unambiguous PDF match"}
            )
            LOGGER.error(
                "[%d/%d] Failed: no unambiguous PDF match",
                article_number,
                len(articles),
            )
            _save_progress_reports(gap_report.to_dict(), manifest, output_path)
            continue
        graph = None
        try:
            LOGGER.info(
                "[%d/%d] Extracting text from %s",
                article_number,
                len(articles),
                pdf_file.name,
            )
            processor = pdf_processor or PDFProcessor()
            markdown = processor.convert_to_markdown(str(pdf_file))
            LOGGER.info(
                "[%d/%d] PDF extraction complete: %d characters",
                article_number,
                len(articles),
                len(markdown),
            )
            graph, decisions = extract_graph_from_markdown(
                markdown, article, config, extractor=extractor, grounder=grounder
            )
            LOGGER.info(
                "[%d/%d] Validating graph: %d node(s), %d edge(s)",
                article_number,
                len(articles),
                len(graph.get("nodes", [])),
                len(graph.get("edges", [])),
            )
            validate_graph(graph)
            graphs.append(graph)
            source = _article_dict(article)
            for node_id, decision in decisions:
                gap_report.add(decision, source, node_id)
            _save_intermediate_result(graph, gap_report.to_dict(), article, output_path)
            manifest["processed"].append({"article": article_key, "pdf": pdf_file.name})
            checkpoint = Consolidator(
                config.output.merge_duplicated_nodes, True
            ).consolidate(graphs)
            validate_graph(checkpoint)
            _save_outputs(checkpoint, gap_report.to_dict(), manifest, output_path)
            LOGGER.info(
                "[%d/%d] Complete; partial and consolidated outputs checkpointed",
                article_number,
                len(articles),
            )
        except Exception as exc:
            failed_path = None
            if graph is not None:
                failed_path = _save_failed_result(
                    graph, article, output_path, exc, traceback.format_exc()
                )
            manifest["failed"].append(
                {
                    "article": article_key,
                    "pdf": pdf_file.name,
                    "error": f"{type(exc).__name__}: {exc}",
                    "failed_graph": str(failed_path) if failed_path else None,
                }
            )
            LOGGER.exception(
                "[%d/%d] Failed while processing %s",
                article_number,
                len(articles),
                pdf_file.name,
            )
            if failed_path:
                LOGGER.error("Invalid graph retained at %s", failed_path)
            _save_progress_reports(gap_report.to_dict(), manifest, output_path)

    LOGGER.info("Consolidating %d article graph(s)", len(graphs))
    consolidated = Consolidator(config.output.merge_duplicated_nodes, True).consolidate(
        graphs
    )
    validate_graph(consolidated)
    _save_outputs(consolidated, gap_report.to_dict(), manifest, output_path)
    LOGGER.info(
        "Finished: %d processed, %d skipped, %d failed; %d node(s), %d edge(s)",
        len(manifest["processed"]),
        len(manifest["skipped"]),
        len(manifest["failed"]),
        len(consolidated.get("nodes", [])),
        len(consolidated.get("edges", [])),
    )
    return manifest


def extract_graph_from_markdown(
    markdown: str,
    article_metadata: Optional[ArticleMetadata],
    config: Config,
    extractor: GraphExtractor,
    grounder: OntologyGrounder,
) -> tuple[dict, list[tuple[str, GroundingDecision]]]:
    """Extract, ground, normalize, and consolidate one Markdown article."""
    source = _article_dict(article_metadata) if article_metadata else {}
    chunker = Chunker(
        max_chunk_size=config.chunking.max_characters_per_chunk,
        overlap_size=config.chunking.overlap_tokens,
        max_sentences=config.chunking.max_sentences_per_chunk,
        max_characters=config.chunking.max_characters_per_chunk,
    )
    chunk_graphs = []
    all_decisions: list[tuple[str, GroundingDecision]] = []
    chunks = chunker.chunk_text(markdown)
    LOGGER.info(
        "Prepared %d text chunk(s): max_characters=%s, max_sentences=%s, overlap=%d",
        len(chunks),
        config.chunking.max_characters_per_chunk or "disabled",
        config.chunking.max_sentences_per_chunk or "disabled",
        config.chunking.overlap_tokens,
    )
    for chunk_number, chunk in enumerate(chunks, 1):
        LOGGER.info(
            "Chunk %d/%d: page=%s section=%s characters=%d; requesting LLM",
            chunk_number,
            len(chunks),
            chunk.page if chunk.page is not None else "unknown",
            chunk.section,
            len(chunk.text),
        )
        draft = extractor.extract(chunk.text, source)
        _enrich_source_spans(draft, chunk.text, chunk.start_char, chunk.page)
        LOGGER.info(
            "Chunk %d/%d: LLM returned %d node(s), %d edge(s); grounding",
            chunk_number,
            len(chunks),
            len(draft.get("nodes", [])),
            len(draft.get("edges", [])),
        )
        grounded_nodes = []
        node_decisions: list[list[GroundingDecision]] = []
        for node in draft.get("nodes", []):
            grounded, decisions = grounder.ground_node(node)
            grounded_nodes.append(grounded)
            node_decisions.append(decisions)
        draft["nodes"] = grounded_nodes
        normalized = normalize_graph(draft, source)
        for normalized_node, decisions in zip(normalized["nodes"], node_decisions):
            all_decisions.extend(
                (normalized_node["id"], decision) for decision in decisions
            )
        chunk_graphs.append(normalized)
        LOGGER.info(
            "Chunk %d/%d complete: %d grounding decision(s)",
            chunk_number,
            len(chunks),
            sum(len(decisions) for decisions in node_decisions),
        )
    if not chunk_graphs:
        return normalize_graph({"nodes": [], "edges": []}, source), []
    return Consolidator().consolidate(chunk_graphs), all_decisions


def extract_graph_from_pdf(
    pdf_path: str,
    article_metadata: Optional[ArticleMetadata] = None,
    config: Optional[Config] = None,
    make_unique: bool = True,
) -> Optional[dict]:
    """Compatibility helper for extracting one PDF."""
    config = config or load_config()
    extractor = GraphExtractor(
        config.llm.endpoint,
        config.llm.model,
        config.llm.api_key,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
        timeout=config.llm.timeout,
        provider=config.llm.provider,
    )
    grounder = OntologyGrounder(
        config.ontology.ols_endpoint,
        config.ontology.elmo_url,
        config.ontology.wikidata_endpoint,
        config.ontology.request_timeout,
        config.ontology.suggestion_threshold,
    )
    markdown = PDFProcessor().convert_to_markdown(pdf_path)
    graph, _ = extract_graph_from_markdown(
        markdown, article_metadata, config, extractor, grounder
    )
    validate_graph(graph)
    return graph


def _find_pdf_for_article(
    article: ArticleMetadata, pdf_files: list[Path]
) -> Optional[Path]:
    """Match an RIS record to a PDF without an unsafe first-file fallback."""
    by_name = {pdf.name.casefold(): pdf for pdf in pdf_files}
    by_stem = {pdf.stem.casefold(): pdf for pdf in pdf_files}
    if article.attachment_path:
        attachment_name = Path(article.attachment_path).name.casefold()
        if attachment_name in by_name:
            return by_name[attachment_name]
    if article.record_id and article.record_id.casefold() in by_stem:
        return by_stem[article.record_id.casefold()]
    if article.doi:
        variants = {
            article.doi.casefold(),
            article.doi.replace("/", "_").casefold(),
            article.doi.replace("/", "-").casefold(),
        }
        matches = [
            pdf
            for pdf in pdf_files
            if any(value in pdf.stem.casefold() for value in variants)
        ]
        if len(matches) == 1:
            return matches[0]
    return None


def _article_dict(article: ArticleMetadata) -> dict:
    return {
        "record_id": article.record_id,
        "title": article.title,
        "year": article.year,
        "doi": article.doi,
        "authors": article.authors,
        "journal": article.journal,
    }


def _enrich_source_spans(
    graph: dict, chunk_text: str, chunk_start: int, page: int | None = None
) -> None:
    for item in [*graph.get("nodes", []), *graph.get("edges", [])]:
        spans = item.get("source_spans") or []
        if not spans and item.get("original_sentence"):
            spans = [{"text": item["original_sentence"]}]
            item["source_spans"] = spans
        for span in spans:
            if not isinstance(span, dict) or not span.get("text"):
                continue
            position = chunk_text.find(span["text"])
            if position >= 0:
                span.setdefault("start_char", chunk_start + position)
                span.setdefault("end_char", chunk_start + position + len(span["text"]))
                resolved_page = page or _page_at_position(chunk_text, position)
                if resolved_page is not None:
                    span.setdefault("paragraph_id", f"page:{resolved_page}")


def _page_at_position(text: str, position: int) -> int | None:
    page = None
    for match in re.finditer(r"(?m)^## Page (\d+)\s*$", text[: position + 1]):
        page = int(match.group(1))
    return page


def _load_partial_results(output_path: Path) -> list[dict]:
    graphs = []
    for path in (
        sorted((output_path / "partial").glob("graph_*.json"))
        if (output_path / "partial").exists()
        else []
    ):
        try:
            graphs.append(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            continue
    return graphs


def _restore_partial_gaps(output_path: Path, report: GapReport) -> None:
    partial = output_path / "partial"
    if not partial.exists():
        return
    for path in partial.glob("gaps_*.json"):
        try:
            for item in json.loads(path.read_text(encoding="utf-8")).get("gaps", []):
                report._records[
                    (item["semantic_role"], normalize_label(item["term"]))
                ] = item
        except (OSError, json.JSONDecodeError, KeyError):
            continue


def _load_processing_manifest(
    output_path: Path, default: dict[str, list[dict]]
) -> dict[str, list[dict]]:
    """Load the last atomic processing checkpoint for a resumed run."""
    path = output_path / "processing_manifest.json"
    if not path.exists():
        return default
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(loaded, dict):
            raise ValueError("manifest root is not an object")
        return {
            key: value if isinstance(value := loaded.get(key), list) else []
            for key in ("processed", "skipped", "failed")
        }
    except (OSError, json.JSONDecodeError, ValueError):
        LOGGER.warning(
            "Could not load prior processing manifest from %s; starting a new one",
            path,
            exc_info=True,
        )
        return default


def _safe_filename(article: ArticleMetadata) -> str:
    value = article.record_id or article.doi or article.title or "unknown"
    return "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in value
    )[:100]


def _save_intermediate_result(
    graph: dict, gaps: dict, article: ArticleMetadata, output_path: Path
) -> None:
    partial = output_path / "partial"
    partial.mkdir(parents=True, exist_ok=True)
    suffix = _safe_filename(article)
    _atomic_json(partial / f"graph_{suffix}.json", graph)
    _atomic_json(partial / f"gaps_{suffix}.json", gaps)


def _save_failed_result(
    graph: dict,
    article: ArticleMetadata,
    output_path: Path,
    error: Exception,
    traceback_text: str,
) -> Path:
    failed = output_path / "failed"
    failed.mkdir(parents=True, exist_ok=True)
    path = failed / f"graph_{_safe_filename(article)}.json"
    _atomic_json(
        path,
        {
            "error": f"{type(error).__name__}: {error}",
            "traceback": traceback_text,
            "graph": graph,
        },
    )
    return path


def _save_outputs(graph: dict, gaps: dict, manifest: dict, output_path: Path) -> None:
    _atomic_json(output_path / "causal_graph.json", graph)
    _atomic_yaml(output_path / "causal_graph.yaml", graph)
    _save_progress_reports(gaps, manifest, output_path)


def _save_progress_reports(gaps: dict, manifest: dict, output_path: Path) -> None:
    """Atomically checkpoint non-graph outputs after every article outcome."""
    _atomic_yaml(output_path / "ontology_gaps.yaml", gaps)
    _atomic_json(output_path / "processing_manifest.json", manifest)
    csv_path = output_path / "ontology_gaps.csv"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", delete=False, dir=output_path, suffix=".tmp"
    ) as handle:
        fields = [
            "term",
            "semantic_role",
            "status",
            "target_ontologies",
            "article_count",
            "occurrence_count",
            "proposed_label",
            "proposed_definition",
            "candidate_parent",
            "review_confidence",
            "candidate_matches",
            "lookup_errors",
            "occurrences",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for gap in gaps.get("gaps", []):
            writer.writerow(
                {
                    key: (
                        json.dumps(gap.get(key), ensure_ascii=False)
                        if isinstance(gap.get(key), (list, dict))
                        else gap.get(key)
                    )
                    for key in fields
                }
            )
        temporary = handle.name
    os.replace(temporary, csv_path)


def _atomic_json(path: Path, value: dict) -> None:
    _atomic_text(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def _atomic_yaml(path: Path, value: dict) -> None:
    _atomic_text(path, yaml.safe_dump(value, sort_keys=False, allow_unicode=True))


def _atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp"
    ) as handle:
        handle.write(text)
        temporary = handle.name
    os.replace(temporary, path)


def _configure_logging(output_path: Path, level: str) -> Path:
    """Log to both the console and an append-only file that survives crashes."""
    output_path.mkdir(parents=True, exist_ok=True)
    log_path = output_path / "processing.log"
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logging.basicConfig(
        level=getattr(logging, level),
        handlers=[console_handler, file_handler],
        force=True,
    )
    return log_path


def main() -> None:
    import argparse

    stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
    stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
    if stdout_reconfigure:
        stdout_reconfigure(encoding="utf-8", errors="replace")
    if stderr_reconfigure:
        stderr_reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(
        description="Extract CAMO graphs and ontology gaps from scientific articles"
    )
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument("--config")
    parser.add_argument("--test-mode", action="store_true")
    parser.add_argument("--max-articles", type=int, default=5)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output folder instead of creating unique",
    )
    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        default="INFO",
        help="Console logging detail (default: INFO)",
    )
    args = parser.parse_args()
    output_path = (
        _make_unique_output_path(args.output_dir)
        if not args.force
        else Path(args.output_dir)
    )
    log_path = _configure_logging(output_path, args.log_level)
    LOGGER.info("CAMO extraction run started; persistent log: %s", log_path)
    manifest = process_folder(
        args.input_dir,
        args.output_dir,
        config_path=args.config,
        test_mode=args.test_mode,
        max_articles=args.max_articles,
        resume=args.resume,
        make_unique=not args.force,
    )
    if manifest["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
