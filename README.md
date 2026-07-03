# Causal Graph Extractor

Extract causal relationships from scientific PDF articles and encode them as structured graphs following the [CAMO (Causal Mosaic)](https://w3id.org/causal-mosaic) schema.

## Overview

This tool processes scientific literature and extracts causal claims into a structured graph format:

1. **PDF → Markdown**: Converts PDFs using Marker (with LLM assist)
2. **Text Chunking**: Splits into context-window-compatible chunks
3. **LLM Extraction**: Uses prompts + LLM to identify causal relationships
4. **Ontology Grounding**: Maps entities to ENVO, BFO, PATO, etc.
5. **Validation**: Checks schema compliance and slot constraints
6. **Consolidation**: Merges across multiple articles
7. **Export**: Outputs JSON + YAML for downstream use

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PDF to Graph Pipeline                    │
├─────────────────────────────────────────────────────────────┤
│ 1. PDF Processor → Markdown (Marker + LLM assist)          │
│ 2. Chunker → Context windows (max 4k chars)                │
│ 3. Graph Extractor → LLM prompts + YAML config             │
│ 4. Validator → Entity grounding + constraint checking       │
│ 5. Consolidator → Merge nodes/edges across articles        │
│ 6. Output → JSON + YAML (CAMO schema)                      │
└─────────────────────────────────────────────────────────────┘
```

## Installation

```bash
# Clone repository
cd /home/ubuntu/repos/camo_extract

# Install dependencies
pip install -r requirements.txt

# Install ontology_agent
pip install -e ontology_agent/

# Install PDF processing (optional, for full functionality)
pip install marker-pdf

# Install development tools
pip install -e .
```

## Configuration

### 1. LLM Settings (`config/llm_settings.yaml`)

```yaml
llm:
  provider: "ollama"
  endpoint: "http://localhost:11434/v1"
  model: "qwen2.5:14b"
  api_key: "${OLLAMA_API_KEY:-}"
  timeout: 600
  temperature: 0.1

chunking:
  max_characters_per_chunk: 4000
  overlap_tokens: 400

output:
  merge_duplicated_nodes: true
  output_formats: ["json", "yaml"]
```

### 2. Prompts (`config/prompts.yaml`)

Externalized LLM instructions with:
- System prompt
- Few-shot examples
- Extraction rules
- Output JSON schema

### 3. Examples (`config/examples.yaml`)

Input-output pairs showing expected behavior.

## Usage

### From Command Line

```bash
# Process all PDFs in a folder
python -m src.main input_dir/ output_dir/

# With custom config
python -m src.main input_dir/ output_dir/ --config config/llm_settings.yaml
```

### From Python

```python
from src import extract_graph_from_pdf, Config, load_config

# Load config
config = load_config("config/llm_settings.yaml")

# Extract from single PDF
graph = extract_graph_from_pdf(
    pdf_path="paper.pdf",
    article_metadata={"title": "My Paper", "year": "2024"},
    config=config,
)

# Save results
import json
with open("output.json", "w") as f:
    json.dump(graph, f, indent=2)
```

### Testing

```bash
# Run quick tests
python3 test_quick.py

# Ruff linting
python3 -m ruff check src/

# Black formatting
python3 -m black src/

# Type checking
python3 -m mypy src/
```

## Input Format

### RIS File

Contains article metadata:

```
TY  - JOUR
TI  - Title of the paper
AU  - Author Name
PY  - 2024
DO  - 10.1234/example
ER  -
```

### PDF Files

Place PDFs in the input directory. The tool matches them to RIS entries by DOI or filename.

## Output Format

```json
{
  "nodes": [
    {
      "id": "node_1",
      "entity": "ENVO:00001001",
      "entity_label": "predator",
      "attribute": "",
      "attribute_label": "",
      "state_qualifier": "removed",
      "entity_type": "management_intervention"
    }
  ],
  "edges": [
    {
      "id": "edge_1",
      "subject_node_id": "node_1",
      "object_node_id": "node_2",
      "predicate": "enables",
      "philosophical_account": "interventionist",
      "features": {
        "direction_status": "asserted",
        "strength_qualitative": "strong"
      },
      "evidence": {
        "type": "quasi_experiment",
        "object": "both"
      },
      "prov": {
        "source_text": "text excerpt",
        "source_page": 5
      }
    }
  ],
  "metadata": {
    "source_count": 1,
    "total_nodes": 1,
    "total_edges": 1
  }
}
```

## Schema Compliance

All outputs follow the [CAMO schema](https://w3id.org/causal-mosaic):

- **Nodes**: Entity + Attribute + State/Change qualifier
- **Edges**: Predicate + Philosophical account + Features + Evidence + Provenance
- **Validation**: Programmatic (ranges, formats) + Ontology (grounding)

## Prompt Externalization

All LLM prompts are stored in YAML for transparency:

- **Changes without code**: Edit `config/prompts.yaml`
- **Few-shot learning**: Add examples to `config/examples.yaml`
- **Reproducibility**: Share prompt configs

See `PROMPT_GUIDE.md` for detailed prompt customization.

## Project Structure

```
camo_extract/
├── config/                      # Configuration
│   ├── prompts.yaml            # LLM prompts (externalized)
│   ├── examples.yaml           # Few-shot examples
│   └── llm_settings.yaml       # LLM & chunking settings
├── data/                        # Input/Output
│   ├── input/                  # RIS + PDFs (test data included)
│   └── output/                 # JSON + YAML graphs
├── ontology_agent/             # Submodule for ontology grounding
├── src/                        # Source code
│   ├── main.py                 # Entry point
│   ├── config.py               # Config management
│   ├── risc_reader.py          # RIS file parsing
│   ├── pdf_processor.py        # PDF → Markdown
│   ├── chunker.py              # Context window management
│   ├── graph_extractor.py      # LLM extraction
│   ├── validator.py            # Schema validation
│   └── consolidator.py         # Graph merging
├── requirements.txt
├── setup.py
├── test_quick.py              # Quick test script
├── PROMPT_GUIDE.md            # Prompt customization guide
└── README.pdf_extractor.md    # This file
```

## Dependencies

- **Core**: pydantic, pyyaml, requests, python-dotenv
- **PDF Processing**: marker-pdf (optional)
- **Ontology**: ontology_agent (installed separately)
- **Dev Tools**: ruff, black, mypy

## Context Window Management

Large documents are chunked to fit LLM context windows:

- **Section-aware**: Preserves document structure
- **Sliding window**: Overlap ensures continuity
- **Configurable**: Adjust chunk size and overlap

## Validation

The validator checks:

- **Entity grounding**: Terms mapped to ontology CURIEs
- **Slot constraints**: Coordinate ranges, numeric ranges
- **Ontology membership**: Entities belong to valid ontologies

## Limitations

- Requires running LLM endpoint (Ollama or compatible)
- PDF conversion quality depends on Marker
- Context window limits require chunking (potential for missing relationships)

## Future Work

- [ ] Support for more chunking strategies (semantic, topic-based)
- [ ] Multi-document reasoning (cross-article edge inference)
- [ ] Confidence scoring per edge
- [ ] Visualization tools (FCM, RAG indices)

## Contributing

1. Run linting: `python3 -m ruff check --fix src/`
2. Run formatting: `python3 -m black src/`
3. Run type checking: `python3 -m mypy src/`
4. Test: `python3 test_quick.py`
5. Submit PR

## License

MIT
