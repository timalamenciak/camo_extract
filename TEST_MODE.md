# Test Mode & Resumable Processing

## Overview

This extractor supports **test mode** and **resumable processing** to make it easy to try out and iterate.

## Test Mode

### Purpose

Test mode allows you to quickly try the system on a subset of articles (default: 5) without processing the entire dataset.

### Usage

```bash
# Test mode with default (5 articles)
python -m src.main input_dir/ output_dir/ --test-mode

# Test mode with custom number of articles
python -m src.main input_dir/ output_dir/ --test-mode --max-articles 3
```

### What Happens in Test Mode

1. Reads first N articles from RIS file (default: 5)
2. Processes each article independently
3. Saves intermediate results to `output_dir/partial/`
4. Outputs final consolidated graph to `output_dir/causal_graph.json` and `.yaml`

### Advantages

- ✅ Quick iteration on prompts and settings
- ✅ Test on real data without waiting for full dataset
- ✅ See progress as each article completes
- ✅ Can stop and resume at any time

## Resumable Processing

### Purpose

If the extraction process is interrupted (e.g., LLM API rate limit, power failure), you can resume where you left off.

### How It Works

1. **Intermediate saves**: Each article's graph is saved to `output_dir/partial/` immediately after extraction
2. **State tracking**: Uses DOI or filename to track which articles have been processed
3. **Resume capability**: On restart, loads existing partial results and skips already-processed articles

### Usage

```bash
# resumed processing automatically starts if partial results exist
python -m src.main input_dir/ output_dir/

# Or explicitly resume
python -m src.main input_dir/ output_dir/ --resume
```

### File Structure

```
output_dir/
├── causal_graph.json      # Final consolidated graph
├── causal_graph.yaml      # Final consolidated graph (YAML)
└── partial/               # Intermediate results (resumable)
    ├── graph_doi_1234.json
    ├── graph_doi_5678.json
    └── ...
```

### Resuming after interruption

1. Check partial results: `ls output_dir/partial/`
2. Review existing output: `cat output_dir/causal_graph.json | head -100`
3. Continue extraction: `python -m src.main input_dir/ output_dir/`

## combined Usage: Test + Resumable

You can use test mode AND resumable processing together:

```bash
# Start test mode (processes 5 articles)
python -m src.main input_dir/ output_dir/ --test-mode

# If interrupted, resume:
python -m src.main input_dir/ output_dir/ --test-mode

# Both will skip already-processed articles
```

## Advanced: Manual Partial Results

### View partial results

```bash
ls output_dir/partial/
# Shows individual graph files for each article
```

### Inspect partial results

```python
from pathlib import Path
import json

partial_dir = Path("output_dir/partial")
for graph_file in partial_dir.glob("*.json"):
    with open(graph_file, "r") as f:
        graph = json.load(f)
        print(f"{graph_file.name}: {len(graph.get('nodes', []))} nodes, {len(graph.get('edges', []))} edges")
```

### Clear partial results and restart

```bash
rm -rf output_dir/partial/
python -m src.main input_dir/ output_dir/
```

## Performance Notes

### Test Mode

- **Fast**: Process 5 articles in minutes (depending on LLM)
- **Debug-friendly**: Easy to inspect intermediate outputs
- **Prompt testing**: Quick feedback loop for prompt iteration

### Resumable Processing

- **Slowest step**: LLM extraction (per article, not chunk)
- **Fast step**: Loading partial results (JSON parse)
- **Memory efficient**: Only full graphs in memory during consolidation

### Time estimates

- **Per article**: 1-10 minutes (depends on PDF size, LLM speed)
- **5 articles (test mode)**: 5-50 minutes
- **Resume overhead**: ~1 second (just loading JSON)

## Troubleshooting

### "Already processed" message

正常 - the system detected you've already processed this article and skipped it.

### Partial results not loading

Check:
1. `output_dir/partial/` exists
2. JSON files are valid (run `python -m json.tool` on them)
3. DOI or filename in graph metadata matches article

### LLM API rate limits

- Use `--test-mode` to process fewer articles
- Increase timeout in `config/llm_settings.yaml`
- Add delay between requests (modifyExtractor class)

### Interrupted mid-process

1. Check `output_dir/partial/` for completed graphs
2. Run again with same output_dir (auto-resumes)
3. Review partial results while remaining articles process

## Example Workflow

### Day 1: Test mode

```bash
# Quick test on 5 articles
python -m src.main data/input/ data/output/ --test-mode

# Review results
cat data/output/causal_graph.json | jq '.metadata, .nodes | length, .edges | length'
```

### Day 2: Full run (interrupted)

```bash
# Start full processing
python -m src.main data/input/ data/output/

# After 10 articles, interrupted by rate limit
```

### Day 2: Resume

```bash
# Resume automatically skips completed articles
python -m src.main data/input/ data/output/

# Total time saved: 10 articles already done!
```

### Day 3: Adjust prompts and retry failed

```bash
# Edit config/prompts.yaml

# Re-run (skips completed, retries failed)
python -m src.main data/input/ data/output/

# Review improvements
cat data/output/causal_graph.json | jq '.edges[] | select(.evidence.certainty_grade == "low")'
```

## Integration with CI/CD

```yaml
# .github/workflows/extract.yml
name: Extract Causal Graphs

on:
  push:
    branches: [main]
  schedule:
    - cron: "0 0 * * *"  # Daily

jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -e ontology_agent/
      
      - name: Run extraction (test mode)
        run: |
          python -m src.main data/input/ data/output/ --test-mode
      
      - name: Save results
        uses: actions/upload-artifact@v3
        with:
          name: causal-graphs
          path: data/output/causal_graph.json
          retention-days: 7
```

## Best Practices

1. **Start with test mode**: Always test on 5 articles first
2. **Check intermediate results**: Review partial graphs as they're created
3. **Use resumable processing**: Let it run, resume if interrupted
4. **Monitor LLM logs**: Check for errors during extraction
5. **Archive partial results**: Backup partial/ directory before retrying

## Future Enhancements

- [ ] Progress bar for extraction
- [ ] Parallel processing (multi-core)
- [ ] Rate limit handling with backoff
- [ ] Automatic retry for failed extractions
- [ ] Summary statistics per article
- [ ] Diff view of prompt changes
