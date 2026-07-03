"""Configuration module for causal graph extraction."""

import os
import re
from pathlib import Path
from typing import Optional

import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """LLM configuration for extraction."""

    provider: str = Field(default="ollama")
    endpoint: str = Field(default="http://localhost:11434/v1")
    model: str = Field(default="qwen2.5:14b")
    api_key: Optional[str] = Field(default=None)
    timeout: int = Field(default=600, ge=10, le=3600)
    temperature: float = Field(default=0.1, ge=0.0, le=1.0)
    max_tokens: int = Field(default=32768, ge=256, le=131072)


class ChunkingConfig(BaseModel):
    """Chunking strategy configuration."""

    max_sentences_per_chunk: Optional[int] = Field(default=None, ge=1, le=1000)
    max_characters_per_chunk: Optional[int] = Field(default=None, ge=100)
    overlap_tokens: int = Field(default=400, ge=0, le=1000)


class OntologyConfig(BaseModel):
    """Ontology grounding configuration."""

    default_ontologies: list[str] = Field(
        default_factory=lambda: ["ELMO", "ENVO", "PATO", "CHEBI", "GO"]
    )
    required_for: list = Field(default=["entity", "attribute"])
    suggestion_threshold: float = Field(default=0.7, ge=0.0, le=1.0)
    ols_endpoint: str = Field(default="https://www.ebi.ac.uk/ols4/api")
    elmo_url: str = Field(
        default="https://raw.githubusercontent.com/timalamenciak/elmo/2026-07-03/elmo.owl"
    )
    wikidata_endpoint: str = Field(default="https://www.wikidata.org/w/api.php")
    request_timeout: int = Field(default=30, ge=5, le=120)
    live_integration_tests: bool = Field(default=False)


class ValidationConfig(BaseModel):
    """Validation thresholds."""

    confidence_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    lat_range: list = Field(default=[-90, 90])
    lon_range: list = Field(default=[-180, 180])
    p_value_range: list = Field(default=[0, 1])
    correlation_range: list = Field(default=[-1, 1])


class OutputConfig(BaseModel):
    """Output format configuration."""

    merge_duplicated_nodes: bool = Field(default=True)


class Config(BaseModel):
    """Main configuration."""

    llm: LLMConfig = Field(default_factory=LLMConfig)
    chunking: ChunkingConfig = Field(default_factory=ChunkingConfig)
    validation: ValidationConfig = Field(default_factory=ValidationConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    ontology: OntologyConfig = Field(default_factory=OntologyConfig)
    data_dir: str = Field(default="data")
    input_dir: str = Field(default="data/input")
    output_dir: str = Field(default="data/output")
    config_dir: str = Field(default="config")


def load_config(config_path: Optional[str] = None) -> Config:
    """Load configuration from YAML file.

    Args:
        config_path: Path to config file. If None, uses environment variable
                    or default location.

    Returns:
        Config instance with validated settings.
    """
    if config_path is None:
        config_path = os.environ.get("CAUSAL_EXTRACT_CONFIG")

    if config_path is None:
        # Default: look in project root
        default_path = Path(__file__).parent.parent / "config" / "llm_settings.yaml"
        if default_path.exists():
            config_path = str(default_path)
        else:
            return Config()

    path = Path(config_path)
    if not path.exists():
        return Config()

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return Config.model_validate(_expand_environment(data))


_ENV_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}")


def _expand_environment(value):
    """Recursively expand ${VAR} and ${VAR:-default} config values."""
    if isinstance(value, dict):
        return {key: _expand_environment(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_expand_environment(item) for item in value]
    if isinstance(value, str):
        return _ENV_PATTERN.sub(
            lambda match: os.environ.get(match.group(1), match.group(2) or ""), value
        )
    return value


def save_config(config: Config, config_path: str) -> None:
    """Save configuration to YAML file.

    Args:
        config: Config instance to save
        config_path: Path to save YAML file
    """
    path = Path(config_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = config.model_dump(mode="json")

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
