# Prompt Guide

## Overview

This extractor uses **externalized prompts** stored in YAML files. This enables:
- **Transparency**: See exactly what instructions the LLM receives
- **Iterative improvement**: Tweak prompts without code changes
- **Reproducibility**: Share prompt configs with collaborators

## Prompt Files

### `config/prompts.yaml`

The main prompt file contains:

1. **System Prompt**: General instructions for the LLM
2. **Few-Shot Examples**: Input-output pairs demonstrating expected behavior
3. **Extraction Instructions**: Detailed rules for extraction
4. **Output Format**: JSON schema guidance

### `config/examples.yaml`

Separate file for few-shot examples, each with:
- `id`: Unique identifier
- `description`: What the example demonstrates
- `input_text`: Excerpt from a paper
- `output_graph`: Expected JSON output

## Prompt Template Variables

Variables in prompts are filled using Jinja2-style syntax:

```yaml
# In prompts.yaml
system_prompt: |
  You are analyzing this article:
  {article_metadata}
  
  Analyze this text chunk:
  {chunk}
```

The `main.py` orchestrator fills these variables when calling the LLM.

## Prompt Customization

### Changing the System Prompt

Edit `config/prompts.yaml`:

```yaml
system_prompt: |
  You are a cautious scientific literature analyst. 
  Only extract relationships that are **explicitly stated**.
  Be conservative: when in doubt, don't extract.
```

### Adding Few-Shot Examples

Add to `config/examples.yaml`:

```yaml
- id: "example_6"
  description: "New pattern example"
  input_text: |
    The data show that...
  output_graph:
    nodes: [...]
    edges: [...]
```

### Adjusting Extraction Rules

Modify `extraction_instructions`:

```yaml
extraction_instructions: |
  # Your custom instructions here
  
  # Important rules:
  1. Only extract direct causal claims
  2. Include all relevant evidence types
  3. Ground entities to ontologies when possible
```

## Prompt Development Workflow

1. **Start with defaults**: Use the included prompts as a baseline
2. **Test on sample paper**: Run extraction and review output
3. **Analyze failures**: Look for:
   - Missing relationships
   - Incorrect entity grounding
   - Wrong philosophical accounts
   - Overly optimistic confidence scores
4. **Tweak prompts**: 
   - Add examples similar to failures
   - Clarify rules
   - Adjust confidence thresholds
5. **Retest**: Verify improvements on the same sample
6. **Iterate**: Repeat until satisfied

## Prompt Best Practices

### Do:
- ✅ Be explicit about what to extract
- ✅ Provide diverse few-shot examples
- ✅ Include negative examples (what NOT to extract)
- ✅ Clarify edge cases
- ✅ Use the exact JSON schema from `causal_mosaic_v0.7.1.yaml`

### Don't:
- ❌ Change the output JSON schema (breaks validation)
- ❌ Use vague language ("extract relationships")
- ❌ Include conflicting instructions
- ❌ Forget to specify temporal/provenance requirements

## Prompt Debugging

### Check the full prompt being sent:

```python
from src import GraphExtractor, load_config

config = load_config()
extractor = GraphExtractor(config_path="config/prompts.yaml")

prompt = extractor._build_prompt("sample text", {"title": "Test"})

print(prompt)
print(f"Character count: {len(prompt)}")
```

### Monitor token usage:

```python
# Estimate tokens (roughly 1 token = 4 chars)
token_count = len(prompt) / 4
print(f"Estimated tokens: {token_count}")

if token_count > config.llm.max_tokens:
    print("Warning: Prompt may exceed context window")
```

## Troubleshooting

### LLM returns non-JSON

**Solution**: Add clearer output format instructions:

```yaml
output_format_instruction: |
  Return ONLY valid JSON.
  Do not include markdown formatting.
  Do not add explanatory text.
```

### Missing entities

**Solution**: Provide better grounding examples:

```yaml
few_shot_examples:
  - input_text: "plant diversity"
    output_graph:
      nodes:
        - entity: "ENVO:0000182"
          entity_label: "plant"
          ...
```

### Wrong philosophical account

**Solution**: Add clearer definitions:

```yaml
system_prompt: |
  Philosophical accounts:
  - counterfactual: "Would E have happened without C?"
  - interventionist: "Can we change E by manipulating C?"
  - probabilistic: "Does C raise the probability of E?"
```

## Updating Prompts

After modifying prompts:

1. **Re-run extraction** on test data
2. **Compare results** before/after
3. **Update examples** if new patterns emerge
4. **Document changes** in version control

## Example: Adding a New Pattern

Goal: Extract relationships about "disturbance events"

1. **Add example** to `config/examples.yaml`:

```yaml
- id: "example_disturbance"
  description: "Disturbance event causal chain"
  input_text: |
    A wildfire burned 500 ha, reducing shrub cover from 80% to 20%.
    Subsequently, grass cover increased from 10% to 40% over two years.
  output_graph:
    nodes:
      - id: "node_fire"
        entity: "BFO:0000015"
        entity_label: "wildfire"
        state_qualifier: "occurred"
        entity_type: "environmental_process"
      - id: "node_shrub"
        entity: "ENVO:0000382"
        entity_label: "shrub"
        attribute: "PATO:0000070"
        attribute_label: "cover"
        state_qualifier: "decreased"
        entity_type: "environmental_variable"
      - id: "node_grass"
        entity: "ENVO:0000382"
        entity_label: "grass"
        attribute: "PATO:0000070"
        attribute_label: "cover"
        state_qualifier: "increased"
        entity_type: "environmental_variable"
    edges:
      - subject_node_id: "node_fire"
        object_node_id: "node_shrub"
        predicate: "causes"
        philosophical_account: "mechanistic"
        evidence: { type: "case_study", object: "both" }
      - subject_node_id: "node_shrub"
        object_node_id: "node_grass"
        predicate: "enables"
        philosophical_account: "mechanistic"
        evidence: { type: "observational_longitudinal", object: "correlation" }
```

2. **Test** on papers with disturbance events
3. **Tune** if needed (add more examples, clarify instructions)

## Advanced: Prompt Layers

For complex tasks, use multiple prompt layers:

```yaml
# Layer 1: Initial extraction
extraction_prompt: |
  Extract all causal relationships...

# Layer 2: Validation
validation_prompt: |
  Review the extracted edges...
  Are all nodes properly grounded?
  Is the direction of causation clear?

# Layer 3: Consensus
consensus_prompt: |
  Compare edges from multiple chunks...
  Merge duplicates...
```

Then chain them in `main.py` or `graph_extractor.py`.
