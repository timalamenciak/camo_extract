# CAMO Extract

CAMO Extract converts RIS-described scientific PDF corpora into a validated
Causal Mosaic graph and an auditable report of literature terms that are not
covered by the preferred ontologies.

## Outputs

Every successful run writes:

- `causal_graph.json` — CAMO v0.7.1 graph
- `causal_graph.yaml` — semantically identical YAML graph
- `ontology_gaps.yaml` — detailed missing/review-needed ontology terms
- `ontology_gaps.csv` — tabular ontology-editor view
- `processing_manifest.json` — processed, skipped, and failed articles
- `partial/` — per-article graphs and gap reports for explicit resume runs

The ontology report separates `exact_match`, `synonym_match`,
`close_match_needs_review`, `no_match`, and `lookup_error`. Network failures are
therefore never reported as missing ontology terms.

## Ontology policy

Grounding is performed after LLM extraction:

| CAMO concept | Preferred sources |
|---|---|
| Taxon | Wikidata |
| Management intervention | ELMO |
| Environmental process | ELMO, then ENVO |
| Environmental variable/entity | ELMO, then ENVO |
| Measured attribute | ELMO, then PATO |

ELMO is pinned to the `2026-07-03` release. Every gap report records the service
URLs and ELMO version used.

## Installation

```powershell
python -m pip install -e .
```

PDF conversion currently uses `pypdf`, which has no OCR models or heavyweight
runtime. It extracts the embedded text layer and emits page headings so page
provenance survives chunking. Scanned/image-only PDFs will fail with a clear
message and should be routed through OCR separately.

## Input layout

Place one RIS file and its PDFs in the same directory. PDF association uses, in
order, RIS `L1`, RIS `ID`, and a unique DOI-derived filename. The extractor never
silently substitutes the first PDF.

```text
input/
  corpus.ris
  ABC123.pdf
  DEF456.pdf
```

## Running

```powershell
python -m src.main input output
python -m src.main input output --test-mode --max-articles 3
python -m src.main input output --resume
```

INFO progress logs are printed for every article and chunk. Use
`--log-level WARNING` for quieter runs or `--log-level DEBUG` when diagnosing a
failure.

Both chunk limits are disabled by default, so a complete article is sent to the
LLM in one request. Set `chunking.max_characters_per_chunk` and/or
`max_sentences_per_chunk` when using a model with a smaller context window.
The default response ceiling is 32,768 tokens to leave room for a complete
article-level graph.

The default LLM configuration targets an OpenAI-compatible Ollama endpoint at
`http://localhost:11434/v1`. Override it in `config/llm_settings.yaml` or with a
custom configuration passed through `--config`.

Resume is explicit: partial results are used only when `--resume` is supplied.
Failures cause a non-zero CLI exit and remain visible in the processing manifest.

## Tests

```powershell
python -m pytest -q
```

The default suite includes CAMO validation, graph reference integrity,
JSON/YAML equivalence, gap-report generation, and RIS-to-PDF checks against the
FACETS test corpus.

Live OLS, ELMO, and Wikidata integration tests are opt-in:

```powershell
$env:RUN_LIVE_ONTOLOGY_TESTS = "1"
python -m pytest -q -m integration tests/test_live_ontology_integrations.py
```

## Validation contract

`causal_mosaic_v0.7.1.yaml` is the authoritative LinkML schema. Graphs are
validated against generated JSON Schema before any final output is replaced.
Additional reference-integrity checks ensure every edge subject and object names
an existing node.
