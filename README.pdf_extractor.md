# PDF-to-Causal-Graph Extractor

Extract causal graphs from scientific PDF articles using LLMs and ontology grounding.

## Overview

This tool extracts causal relationships from scientific literature and encodes them as structured graphs following the [CAMO (Causal Mosaic)](https://w3id.org/causal-mosaic) schema. The pipeline:

1. **PDF → Markdown** using Marker (with LLM assist for tables/figures)
2. **Text Chunking** to fit context windows
3. **LLM Extraction** to identify causal relationships
4. **Ontology Grounding** using the ontology_agent
5. **Validation** of extracted entities and slot values
6. **Consolidation** across multiple articles

## Installation

```bash
# Install core dependencies
pip install -r requirements.txt

# Install ontology_agent
pip install -e ontology_agent/

# Optional: Install for PDF processing
pip install marker-pdf
```

## Configuration

Create a config file at `config/llm_settings.yaml`:

```yaml
llm:
  provider: "ollama"
  endpoint: "http://localhost:11434/v1"
  model: "qwen2.5:14b"
  api_key: "${OLLAMA_API_KEY:-}"
  timeout: 600
  temperature: 0.1

chunking:
  max_sentences_per_chunk: 10
  max_characters_per_chunk: 4000
  min_sentences: 3
  min_characters: 200

output:
  merge_duplicated_nodes: true
  output_formats: ["json", "yaml"]
```

## Usage

### From Command Line

```bash
# Process all PDFs in a folder with RIS metadata
python -m src.main /path/to/input /path/to/output

# With custom config
python -m src.main /path/to/input /path/to/output --config config/llm_settings.yaml
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

## Input Format

### RIS File

The tool expects a RIS file with article metadata:

```
TY  - JOUR
TI  - Title of the paper
AU  - Author Name
PY  - 2024
DO  - 10.1234/example
ER  -
```

### PDF Files

Place PDF files in the input directory alongside the RIS file. The tool matches PDFs to RIS entries by DOI or filename.

## Output Format

The tool outputs both JSON and YAML with the CAMO schema:

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
      "features": { ... },
      "evidence": { ... },
      "prov": { "source_text": "...", "source_page": 5 }
    }
  ],
  "metadata": {
    "source_count": 1,
    "total_nodes": 1,
    "total_edges": 1
  }
}
```

## Prompt Externalization

All LLM prompts are externalized in `config/prompts.yaml`:

- **system_prompt**: General instructions
- **few_shot_examples**: Examples of expected input/output
- **extraction_instructions**: Extraction rules
- **output_format_instruction**: JSON schema guidance

This enables transparency and easy modification without code changes.

## Ontology Grounding

Entities are grounded to ontologies using the `ontology_agent`:

- **ENVO**: Environmental entities
- **BFO**: Basic Formal Ontology
- **PATO**: Phenotypic qualities
- **CHEBI**: Chemical entities
- **GO**: Gene Ontology

## Context Window Management

Large documents are chunked to fit the LLM context window:

- **Section-aware chunking**: Preserves document structure
- **Sliding window**: Overlap between chunks ensures continuity
- **Configurable**: Adjust chunk size in config

## Validation

The validator checks:

- **Entity grounding**: Terms are mapped to ontology CURIEs
- **Slot constraints**: Coordinate ranges, numeric ranges
- **Ontology membership**: Entities belong to valid ontologies

## Project Structure

```
camo_extract/
├── config/
│   ├── prompts.yaml          # LLM prompts (externalized)
│   ├── examples.yaml         # Few-shot examples
│   └── llm_settings.yaml     # LLM & chunking settings
├── data/
│   ├── input/               # RIS + PDFs
│   └── output/              # JSON + YAML graphs
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── config.py            # Config management
│   ├── risc_reader.py       # RIS parsing
│   ├── pdf_processor.py     # PDF → Markdown
│   ├── chunker.py           # Context window management
│   ├── graph_extractor.py   # LLM extraction
│   ├── validator.py         # Schema validation
│   └── consolidator.py      # Graph merging
├── ontology_agent/          # Submodule
├── requirements.txt
└── README.md
```

## Limitations

- Requires running LLM endpoint (Ollama or compatible)
- PDF conversion quality depends on Marker
- Context window limits require chunking (potential for missing relationships)

## Future Work

- [ ] Support for more chunking strategies (semantic, topic-based)
- [ ] Multi-document reasoning (cross-article edge inference)
- [ ] Confidence scoring per edge
- [ ] Visualization tools (FCC, RAG indices)
