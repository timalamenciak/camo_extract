"""LLM extraction of CAMO graph drafts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import yaml
from openai import OpenAI


class GraphExtractor:
    """Extract raw graph structure; ontology grounding is a separate stage."""

    def __init__(
        self,
        llm_endpoint: str = "http://localhost:11434/v1",
        llm_model: str = "qwen2.5:14b",
        api_key: Optional[str] = None,
        config_path: Optional[str] = None,
        temperature: float = 0.1,
        max_tokens: int = 4096,
        timeout: int = 600,
        provider: str = "ollama",
    ):
        if provider not in {"ollama", "openai", "openai_compatible"}:
            raise ValueError(f"Unsupported LLM provider: {provider}")
        self.provider = provider
        self.llm_endpoint = llm_endpoint
        self.llm_model = llm_model
        self.api_key = api_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.prompts = self._load_prompts(config_path)

    def extract(self, text: str, article_metadata: Optional[dict] = None) -> dict:
        response = self._call_llm(self._build_prompt(text, article_metadata))
        return self._parse_response(response)

    def _load_prompts(self, config_path: Optional[str]) -> dict:
        path = (
            Path(config_path)
            if config_path
            else Path(__file__).parent.parent / "config" / "prompts.yaml"
        )
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        return {
            "system": data.get("system_prompt", ""),
            "few_shot": data.get("few_shot_examples", ""),
            "instructions": data.get("extraction_instructions", ""),
            "format": data.get("output_format_instruction", ""),
        }

    def _build_prompt(self, text: str, metadata: Optional[dict]) -> str:
        parts = [self.prompts["system"]]
        if self.prompts["few_shot"]:
            parts.extend(["# Examples", self.prompts["few_shot"]])
        if metadata:
            parts.extend(["# Article", json.dumps(metadata, ensure_ascii=False)])
        parts.extend(
            ["# Text", text, self.prompts["instructions"], self.prompts["format"]]
        )
        return "\n\n".join(part for part in parts if part)

    def _call_llm(self, prompt: str) -> str:
        client = OpenAI(
            base_url=self.llm_endpoint,
            api_key=self.api_key or "not-needed",
            timeout=self.timeout,
        )
        response = client.chat.completions.create(
            model=self.llm_model,
            messages=[
                {"role": "system", "content": "Return only valid JSON."},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("LLM returned an empty response")
        return content

    @staticmethod
    def _parse_response(response: str) -> dict:
        stripped = response.strip()
        if stripped.startswith("```"):
            stripped = stripped.split("\n", 1)[-1].rsplit("```", 1)[0]
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            start, end = stripped.find("{"), stripped.rfind("}")
            if start < 0 or end <= start:
                raise ValueError("LLM response did not contain a JSON object")
            parsed = json.loads(stripped[start : end + 1])
        if (
            not isinstance(parsed, dict)
            or not isinstance(parsed.get("nodes", []), list)
            or not isinstance(parsed.get("edges", []), list)
        ):
            raise ValueError("LLM response is not a graph object")
        return parsed
