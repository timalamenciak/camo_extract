# PDF Causal Graph Extractor - Complete Package

## What Was Built

A complete system to extract causal graphs from scientific PDF articles with:

### ✅ Core Features

1. **PDF Processing** - Converts PDFs to Markdown using Marker
2. **Text Chunking** - Manually chunks to fit context windows
3. **LLM Extraction** - Uses externalized prompts from YAML
4. **Ontology Grounding** - Uses ontology_agent for entity grounding
5. **Validation** - Programmatic + ontology validation
6. **Consolidation** - Merges multiple articles into single graph
7. **Test Mode** - Process first N articles (default: 5)
8. **Resumable Processing** - Saves intermediate results, auto-resumes

### ✅ File Structure

```
causal_extract/
├── config/                           # Configuration
│   ├── prompts.yaml                 # LLM prompts (externalized)
│   ├── examples.yaml                # Few-shot examples
│   └── llm_settings.yaml            # LLM & chunking settings
├── data/
│   ├── input/                       # RIS + PDFs
│   └── output/                      # JSON + YAML (test generated)
├── ontology_agent/                  # Submodule for ontology grounding
├── src/                             # Source code
│   ├── __init__.py
│   ├── main.py                      # Entry point + resumability
│   ├── config.py                    # Config management
│   ├── risc_reader.py               # RIS file parsing
│   ├── pdf_processor.py             # PDF → Markdown
│   ├── chunker.py                   # Context window management
│   ├── graph_extractor.py           # LLM extraction
│   ├── validator.py                 # Schema validation
│   └── consolidator.py              # Graph merging
├── requirements.txt                 # Dependencies
├── setup.py                         # Package installation
├── test_quick.py                    # Quick tests
├── PROMPT_GUIDE.md                  # Prompt customization guide
├── TEST_MODE.md                     # Test mode & resumability guide
├── README.pdf_extractor.md          # Technical documentation
└── README.md                        # User-facing overview
```

### ✅ Key Features Implemented

1. **Externalized Prompts**
   - All prompts in YAML (`config/prompts.yaml`)
   - Few-shot examples in `config/examples.yaml`
   - Easy to modify without code changes

2. **Context Window Management**
   - Manual chunking (not LLM-assisted)
   - Configurable chunk size (default: 4000 chars)
   - Section-aware splitting

3. **Test Mode**
   - `--test-mode` flag to process first N articles
   - Default: 5 articles
   - Customizable with `--max-articles N`

4. **Resumable Processing**
   - Saves intermediate results to `output_dir/partial/`
   - Auto-detects and skips already-processed articles
   - Can be interrupted and resumed

5. **Validation**
   - Programmatic: coordinate ranges, numeric ranges
   - Ontology: grounding to ENVO, BFO, PATO, etc.

6. **RIS File Handling**
   - Parses article metadata
   - Matches PDFs by DOI or filename

7. **Output**
   - JSON: `causal_graph.json`
   - YAML: `causal_graph.yaml`
   - Both following CAMO schema

### ✅ Testing & Quality

- **Linting**: All passes with `ruff check --fix`
- **Formatting**: All passes with `black`
- **Type Checking**: All passes with `mypy`
- **Quick Tests**: All pass with `test_quick.py`

### ✅ Usage

```bash
# Quick test on first 5 articles
python -m src.main data/input data/output --test-mode

# Full processing with resumability
python -m src.main data/input data/output

# Resume interrupted processing (auto-detects partial results)
python -m src.main data/input data/output

# Custom config
python -m src.main data/input data/output --config config/llm_settings.yaml
```

### ✅ Documentation

- `README.pdf_extractor.md` - Technical details
- `README.md` - User-facing overview
- `PROMPT_GUIDE.md` - Prompt customization
- `TEST_MODE.md` - Test mode & resumability guide
- Inline code comments

### ✅ Dependencies

- `pydantic>=2.0`
- `pyyaml>=6.0`
- `requests>=2.31`
- `python-dotenv>=1.0`
- `marker-pdf>=1.0` (for PDF processing)
- `ontology-agent>=0.1.0` (for ontology grounding)

### ✅ Next Steps

To use with real PDFs:

1. Place PDFs in `data/input/`
2. Ensure PDFs match RIS entries by DOI
3. Run extraction
4. Review results in `data/output/`

### ✅ What's Included

- ✅ Complete working code
- ✅ Externalized prompts
- ✅ Test mode (process first N articles)
- ✅ Resumable processing
- ✅ RIS file reading
- ✅ Context window chunking
- ✅ Ontology grounding
- ✅ Validation
- ✅ Consolidation
- ✅ JSON + YAML output
- ✅ Full documentation
- ✅ All linting/type checks pass
