"""Configuration management for ontology agent.

Supports loading configuration from YAML files with support for:
- LLM endpoint configuration
- Custom ontology sources (OWL files via URL)
- Override of default OLS/BioPortal settings
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """LLM endpoint configuration."""

    endpoint: str = Field(description="LLM endpoint URL")
    model: str | None = Field(default=None, description="Model name to use")
    api_key: str | None = Field(default=None, description="API key for LLM")
    timeout: int = Field(
        default=30, ge=5, le=120, description="Request timeout in seconds"
    )


class CustomOntology(BaseModel):
    """Custom ontology source not listed on OLS/BioPortal."""

    name: str = Field(description="Ontology name/identifier")
    url: str = Field(description="URL to OWL file")
    prefix: str = Field(description="Ontology prefix (e.g., MYONTO)")
    description: str | None = Field(default=None, description="Ontology description")


class AgentConfig(BaseModel):
    """Main agent configuration."""

    llm: LLMConfig | None = Field(
        default=None, description="LLM endpoint configuration"
    )
    custom_ontologies: list[CustomOntology] = Field(
        default_factory=list, description="Custom ontology sources"
    )
    ols_endpoint: str = Field(
        default="https://www.ebi.ac.uk/ols4/api", description="OLS API endpoint"
    )
    bioportal_endpoint: str = Field(
        default="https://data.bioontology.org",
        description="BioPortal API endpoint",
    )
    bioportal_api_key: str | None = Field(default=None, description="BioPortal API key")
    fallback_to_suggestions: bool = Field(
        default=True, description="Fall back to term suggestions when no match found"
    )


def load_config(config_path: str | None = None) -> AgentConfig:
    """Load configuration from YAML file.

    Args:
        config_path: Path to YAML config file. If None, checks:
            - ONT_AGENT_CONFIG environment variable
            - Default: .ontology-agent/config.yaml

    Returns:
        Configured AgentConfig instance
    """
    if config_path is None:
        config_path = os.environ.get("ONT_AGENT_CONFIG")

    if config_path is None:
        config_path = os.path.join(
            os.path.expanduser("~"), ".ontology-agent", "config.yaml"
        )

    path = Path(config_path)

    if path.exists():
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        return AgentConfig.model_validate(data)

    return AgentConfig()


def save_config(config: AgentConfig, config_path: str) -> None:
    """Save configuration to YAML file.

    Args:
        config: AgentConfig instance to save
        config_path: Path to save YAML file
    """
    path = Path(config_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = config.model_dump(mode="json", exclude_none=True)

    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
