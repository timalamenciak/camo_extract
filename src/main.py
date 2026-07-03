"""Command-line orchestration for CAMO extraction."""

from __future__ import annotations

import csv
import json
import os
import sys
import tempfile
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
) -> dict:
    """Process an RIS-described PDF corpus and return a processing manifest."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
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
    graphs = list(existing_graphs)

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

    for article in articles:
        article_key = article.doi or article.record_id or article.title or "unknown"
        if resume and (
            (article.doi and article.doi in processed_keys)
            or article.title in processed_keys
        ):
            manifest["skipped"].append(
                {"article": article_key, "reason": "already processed"}
            )
            continue
        pdf_file = _find_pdf_for_article(article, pdf_files)
        if pdf_file is None:
            manifest["failed"].append(
                {"article": article_key, "error": "No unambiguous PDF match"}
            )
            continue
        try:
            processor = pdf_processor or PDFProcessor(use_llm_assist=False)
            markdown = processor.convert_to_markdown(str(pdf_file))
            graph, decisions = extract_graph_from_markdown(
                markdown, article, config, extractor=extractor, grounder=grounder
            )
            validate_graph(graph)
            graphs.append(graph)
            source = _article_dict(article)
            for node_id, decision in decisions:
                gap_report.add(decision, source, node_id)
            _save_intermediate_result(graph, gap_report.to_dict(), article, output_path)
            manifest["processed"].append({"article": article_key, "pdf": pdf_file.name})
        except Exception as exc:
            manifest["failed"].append(
                {
                    "article": article_key,
                    "pdf": pdf_file.name,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )

    consolidated = Consolidator(config.output.merge_duplicated_nodes, True).consolidate(
        graphs
    )
    validate_graph(consolidated)
    _save_outputs(consolidated, gap_report.to_dict(), manifest, output_path)
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
    for chunk in chunker.chunk_text(markdown):
        draft = extractor.extract(chunk.text, source)
        _enrich_source_spans(draft, chunk.text, chunk.start_char)
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
    if not chunk_graphs:
        return normalize_graph({"nodes": [], "edges": []}, source), []
    return Consolidator().consolidate(chunk_graphs), all_decisions


def extract_graph_from_pdf(
    pdf_path: str,
    article_metadata: Optional[ArticleMetadata] = None,
    config: Optional[Config] = None,
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
    markdown = PDFProcessor(use_llm_assist=False).convert_to_markdown(pdf_path)
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


def _enrich_source_spans(graph: dict, chunk_text: str, chunk_start: int) -> None:
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


def _save_outputs(graph: dict, gaps: dict, manifest: dict, output_path: Path) -> None:
    _atomic_json(output_path / "causal_graph.json", graph)
    _atomic_yaml(output_path / "causal_graph.yaml", graph)
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
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp"
    ) as handle:
        handle.write(text)
        temporary = handle.name
    os.replace(temporary, path)


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
    args = parser.parse_args()
    manifest = process_folder(
        args.input_dir,
        args.output_dir,
        config_path=args.config,
        test_mode=args.test_mode,
        max_articles=args.max_articles,
        resume=args.resume,
    )
    if manifest["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
