# Configuration Features

## Overview

The ontology_agent now supports configuration via YAML files, allowing customization of:

1. **LLM endpoint** - For term suggestion generation
2. **Custom ontologies** - OWL files from URLs not listed on OLS/BioPortal
3. **Endpoints** - Override default OLS/BioPortal URLs
4. **Settings** - Control fallback behavior and API keys

## Configuration File

### Location

Configuration is loaded from:
1. Environment variable `ONT_AGENT_CONFIG` (if set)
2. Default: `~/.ontology-agent/config.yaml`

### Example Configuration

```yaml
llm:
  endpoint: "https://api.openai.com/v1/chat/completions"
  model: "gpt-4"
  api_key: "${LLM_API_KEY}"  # Can reference env vars
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

### Configuration Sections

#### LLM Configuration
- `endpoint`: LLM API endpoint URL
- `model`: Model name (optional)
- `api_key`: API key (optional, can use env var)
- `timeout`: Request timeout in seconds

#### Custom Ontologies
- `name`: Unique identifier for the ontology
- `url`: URL to the OWL file
- `prefix`: Ontology prefix (e.g., "MY")
- `description`: Human-readable description (optional)

#### Endpoints
- `ols_endpoint`: OLS API endpoint
- `bioportal_endpoint`: BioPortal API endpoint
- `bioportal_api_key`: BioPortal API key (optional)

#### Settings
- `fallback_to_suggestions`: Whether to generate suggestions on no match

## Usage

### Python API

```python
from ontology_agent import OntologyAgent

# Load config from default location
agent = OntologyAgent()

# Or specify custom config path
agent = OntologyAgent(config_path="/path/to/config.yaml")

# Search will use configured endpoints and ontologies
result = agent.search("temperate grassland")
```

### Command-line

```bash
# Use default config location
ontology-agent search "temperate grassland"

# Specify custom config
ontology-agent search "temperate grassland" --config /path/to/config.yaml
```

## Custom Ontologies

To add ontologies not on OLS/BioPortal:

1. Host your OWL file at a stable URL
2. Add to config:

```yaml
custom_ontologies:
  - name: "MYONTO"
    url: "https://example.com/myontology.owl"
    prefix: "MY"
```

Note: Full text search within custom ontologies requires OWL parsing (rdflib/owlready2).
The current implementation provides framework support - full parsing would need to be implemented.

## Environment Variables

You can reference environment variables in your config using `${VAR_NAME}` syntax:

```yaml
llm:
  api_key: "${LLM_API_KEY}"

bioportal_api_key: "${BIOPORTAL_API_KEY}"
```

Or set them directly:
```bash
export LLM_API_KEY="your-key-here"
export BIOPORTAL_API_KEY="your-key-here"
```

## API

### Configuration Functions

- `load_config(path=None)`: Load config from file or default location
- `save_config(config, path)`: Save config to file
- `AgentConfig`: Pydantic model for configuration
- `CustomOntology`: Pydantic model for custom ontology entries
- `LLMConfig`: Pydantic model for LLM configuration

### Agent Constructor

```python
OntologyAgent(
    parameters=None,    # SearchParameters override
    config=None,        # AgentConfig object
    config_path=None    # Path to config file
)
```

If both `config` and `config_path` are None, default config is loaded.
If `config` is provided, it takes precedence over `config_path`.
