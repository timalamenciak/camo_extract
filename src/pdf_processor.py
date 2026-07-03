"""PDF-to-Markdown conversion using Marker's supported Python API."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from typing import Optional

HAS_MARKER = importlib.util.find_spec("marker") is not None


class PDFProcessor:
    """Convert a PDF to Markdown while keeping heavyweight imports lazy."""

    def __init__(self, use_llm_assist: bool = False):
        if not HAS_MARKER:
            raise ImportError(
                "marker-pdf is not installed. Install with: "
                "pip install 'marker-pdf>=1.10'"
            )
        self.use_llm_assist = use_llm_assist

    def convert_to_markdown(
        self, pdf_path: str, output_dir: Optional[str] = None
    ) -> str:
        path = Path(pdf_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        from marker.config.parser import ConfigParser
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered

        config_parser = ConfigParser(
            {"output_format": "markdown", "use_llm": self.use_llm_assist}
        )
        converter = PdfConverter(
            config=config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
            processor_list=config_parser.get_processors(),
            renderer=config_parser.get_renderer(),
            llm_service=(
                config_parser.get_llm_service() if self.use_llm_assist else None
            ),
        )
        rendered = converter(str(path))
        markdown, _, _ = text_from_rendered(rendered)
        markdown = self._clean_md(markdown)
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            (output_path / f"{path.stem}.md").write_text(markdown, encoding="utf-8")
        return markdown

    @staticmethod
    def _clean_md(markdown: str) -> str:
        markdown = re.sub(r"^{%.*%}$", "", markdown, flags=re.MULTILINE)
        return re.sub(r"\n\n\n+", "\n\n", markdown).strip()
