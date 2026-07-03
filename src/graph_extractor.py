"""Causal graph extractor using LLMs and ontologies."""

import json
from pathlib import Path
from typing import Optional
import yaml  # type: ignore[import-untyped]
import requests  # type: ignore[import-untyped]

try:
    from ontology_agent import OntologyAgent  # type: ignore[attr-defined]

    HAS_ONTOLOGY_AGENT = True
except ImportError:
    HAS_ONTOLOGY_AGENT = False

    class OntologyAgent:  # type: ignore[no-redef]
        pass


try:
    from openai import OpenAI  # type: ignore[import-untyped, import-not-found]

    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    OpenAI = None


class GraphExtractor:
    """Extract causal graphs from text using LLMs and ontologies."""

    def __init__(
        self,
        llm_endpoint: str = "http://localhost:11434/v1",
        llm_model: str = "qwen2.5:14b",
        api_key: Optional[str] = None,
        config_path: Optional[str] = None,
    ):
        """Initialize graph extractor.

        Args:
            llm_endpoint: LLM API endpoint
            llm_model: Model name
            api_key: API key (if needed)
            config_path: Path to config file with prompts
        """
        self.llm_endpoint = llm_endpoint
        self.llm_model = llm_model
        self.api_key = api_key

        # Load prompts from config
        self.prompts = self._load_prompts(config_path)

        # Initialize ontology agent
        self.ontology_agent = None
        if HAS_ONTOLOGY_AGENT:
            self.ontology_agent = OntologyAgent()

    def extract(
        self,
        text: str,
        article_metadata: Optional[dict] = None,
    ) -> dict:
        """Extract causal graph from text.

        Args:
            text: Text to analyze
            article_metadata: Optional article metadata dict

        Returns:
            Graph dict with nodes and edges
        """
        # Build prompt
        prompt = self._build_prompt(text, article_metadata)

        # Call LLM
        response = self._call_llm(prompt)

        # Parse response
        graph = self._parse_response(response)

        # Validate and ground
        graph = self._validate_and_ground(graph)

        return graph

    def _load_prompts(self, config_path: Optional[str]) -> dict:
        """Load prompts from config file."""
        prompts = {
            "system": "",
            "few_shot": "",
            "instructions": "",
            "format": "",
        }

        if config_path is None:
            config_path_str = str(
                Path(__file__).parent.parent / "config" / "prompts.yaml"
            )
        else:
            config_path_str = str(config_path)

        if Path(config_path_str).exists():
            with open(config_path_str, "r") as f:
                data = yaml.safe_load(f)  # type: ignore

            prompts["system"] = data.get("system_prompt", "")
            prompts["few_shot"] = data.get("few_shot_examples", "")
            prompts["instructions"] = data.get("extraction_instructions", "")
            prompts["format"] = data.get("output_format_instruction", "")

        return prompts

    def _build_prompt(self, text: str, metadata: Optional[dict]) -> str:
        """Build prompt from components."""
        parts = []

        # System prompt
        if self.prompts["system"]:
            parts.append(self.prompts["system"])

        # Few-shot examples
        if self.prompts["few_shot"]:
            parts.append("# Few-Shot Examples")
            parts.append(self.prompts["few_shot"])

        # Context info
        if metadata:
            parts.append("# Article Context")
            parts.append(f"Title: {metadata.get('title', 'N/A')}")
            parts.append(f"Year: {metadata.get('year', 'N/A')}")
            parts.append(f"DOI: {metadata.get('doi', 'N/A')}")
            parts.append("")

        # Text chunk
        parts.append("# Text Chunk to Analyze")
        parts.append("```markdown")
        parts.append(text)
        parts.append("```")
        parts.append("")

        # Instructions
        if self.prompts["instructions"]:
            parts.append(self.prompts["instructions"])

        # Output format
        if self.prompts["format"]:
            parts.append(self.prompts["format"])

        return "\n".join(parts)

    def _call_llm(self, prompt: str) -> str:
        """Call LLM with prompt."""
        # Try Ollama API
        if self.llm_endpoint and "ollama" in self.llm_endpoint:
            return self._call_ollama(prompt)

        # Try OpenAI-compatible API
        if HAS_OPENAI:
            try:
                client = OpenAI(
                    base_url=self.llm_endpoint, api_key=self.api_key or "not-needed"
                )

                response = client.chat.completions.create(
                    model=self.llm_model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a scientific literature analyst.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.1,
                    max_tokens=4096,
                )

                return response.choices[0].message.content

            except Exception as e:
                raise RuntimeError(f"LLM API call failed: {e}")

        raise RuntimeError("No LLM backend available")

    def _call_ollama(self, prompt: str) -> str:
        """Call Ollama API."""
        url = f"{self.llm_endpoint}/chat"

        payload = {
            "model": self.llm_model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a scientific literature analyst.",
                },
                {"role": "user", "content": prompt},
            ],
            "options": {
                "temperature": 0.1,
            },
        }

        try:
            response = requests.post(url, json=payload, timeout=600)  # type: ignore
            response.raise_for_status()

            data = response.json()
            return data.get("message", {}).get("content", "")

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Ollama API call failed: {e}")

    def _parse_response(self, response: str) -> dict:
        """Parse LLM response into graph dict."""
        # Try to extract JSON from response
        try:
            # Try direct JSON parsing
            start = response.find("{")
            end = response.rfind("}") + 1

            if start >= 0 and end > start:
                json_str = response[start:end]
                return json.loads(json_str)

            # Try to parse the whole response
            return json.loads(response)

        except json.JSONDecodeError:
            # Fallback: attempt to fix common issues
            json_str = response.strip()

            # Try to find JSON block
            if "```json" in json_str:
                json_str = json_str.split("```json")[1]
                json_str = json_str.split("```")[0]
            elif "```" in json_str:
                json_str = json_str.split("```")[1]
                if "```" in json_str:
                    json_str = json_str.split("```")[0]

            try:
                return json.loads(json_str.strip())
            except json.JSONDecodeError:
                # Return empty graph
                return {
                    "nodes": [],
                    "edges": [],
                    "metadata": {
                        "error": "Failed to parse JSON from LLM response",
                        "raw_response": response[:500],
                    },
                }

    def _validate_and_ground(self, graph: dict) -> dict:
        """Validate and ground entities in graph."""
        if not self.ontology_agent:
            return graph

        # Ground each node's entity
        for node in graph.get("nodes", []):
            entity = node.get("entity", "")
            if entity and not entity.startswith(
                ("ENVO:", "BFO:", "PATO:", "CHEBI:", "GO:")
            ):
                # Try to ground using ontology agent
                result = self.ontology_agent.search(entity, limit=1)
                if result.results and result.results[0].term:
                    node["entity"] = result.results[0].term.curie
                    node["entity_label"] = result.results[0].term.label

        # Ground attributes
        for node in graph.get("nodes", []):
            attribute = node.get("attribute", "")
            if attribute and not attribute.startswith("PATO:"):
                result = self.ontology_agent.search(
                    attribute, ontologies=["PATO"], limit=1
                )
                if result.results and result.results[0].term:
                    node["attribute"] = result.results[0].term.curie
                    if "attribute_label" not in node:
                        node["attribute_label"] = result.results[0].term.label

        return graph
