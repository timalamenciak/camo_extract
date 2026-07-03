# Ontology Agent

Standalone ontology lookup agent with term suggestion capabilities.

## Installation

```bash
pip install -e .
```

## Usage

### Python API

```python
from ontology_agent import OntologyAgent

agent = OntologyAgent()

# Basic search
result = agent.search("temperate grassland")

# Search with preferred ontology
result = agent.search("cell division", preferred_ontology="GO")

# Getterm by CURIE
result = agent.find_term_by_curie("ENVO:00001001")

# Check the result
if result.status == "found":
    print(f"Found: {result.results[0].results[0].term.label}")
else:
    print("No match found")
    for suggestion in result.results[0].suggestions:
        print(f"Suggest: {suggestion.term} in {suggestion.ontology}")
```

### Command-line Interface

```bash
# Search for a term
ontology-agent search "temperate grassland"

# Search with preferred ontology
ontology-agent search "cell division" --ontology GO

# Getterm by CURIE
ontology-agent term ENVO:00001001

# Verbose output
ontology-agent search "temperate grassland" --verbose

# JSON output
ontology-agent search "temperate grassland" --json

# With config file
ontology-agent search "temperate grassland" --config ~/.ontology-agent/config.yaml
```

## Term Suggestion

When no appropriate term is found, the agent generates suggestions including:

- **Suggested term label** - Refined term based on query analysis
- **Recommended ontology** - ENVO, BFO, PATO, etc.
- **BFO hierarchy position** - Parent class in Basic Formal Ontology
- **Proposed definition** - Ontology-appropriate definition

## Configuration

The agent can be configured via YAML file or environment variables:

### YAML Configuration

Create a config file at `~/.ontology-agent/config.yaml` or set `ONT_AGENT_CONFIG`:

```yaml
llm:
  endpoint: "https://api.openai.com/v1/chat/completions"
  model: "gpt-4"
  api_key: "${LLM_API_KEY}"
  timeout: 60

custom_ontologies:
  - name: "MYONTO"
    url: "https://example.com/myontology.owl"
    prefix: "MY"
    description: "My custom ontology"

ols_endpoint: "https://www.ebi.ac.uk/ols/api"
bioportal_endpoint: "https://data.bioontology.bioontology.org"
bioportal_api_key: "${BIOPORTAL_API_KEY}"
fallback_to_suggestions: true
```

### Environment Variables

- `ONT_AGENT_CONFIG`: Path to YAML config file
- `LLM_API_KEY`: LLM API key for term generation
- `BIOPORTAL_API_KEY`: API key for BioPortal access (optional)

## Multiple Ontology Sources

The agent queries both:

- **OLS** (Ontology Lookup Service) - EMBL-EBI
- **BioPortal** - NIH-funded repository
- **Custom ontologies** - Your own OWL files via URL

It uses first successful source and falls back to suggestions if needed.

## Custom Ontologies

To add ontologies not listed on OLS/BioPortal:

1. Host your OWL file at a URL
2. Add it to the `custom_ontologies` section in config
3. Specify a unique name, URL, and prefix

```yaml
custom_ontologies:
  - name: "MYONTO"
    url: "https://example.com/myontology.owl"
    prefix: "MY"
```

## BFO Hierarchy

The agent maps terms to BFO (Basic Formal Ontology) classes:

- **BFO:0000002** - Continuant (entities that exist at a time)
- **BFO:0000003** - Occurrent (processes, events)
- **BFO:0000004** - Independent continuant (material entities)
- **BFO:0000015** - Process
- **BFO:0000020** - Quality

## License

MIT
