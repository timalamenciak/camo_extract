"""PDF to Markdown converter using Marker."""

from pathlib import Path
from typing import Optional
import re

HAS_MARKER = False
try:
    from marker.convert import convert_single_pdf  # type: ignore[import-untyped, import-not-found]
    from marker.output import convert_document_to_markdown  # type: ignore[import-untyped, import-not-found]

    HAS_MARKER = True
except ImportError:
    pass


class PDFProcessor:
    """Converter from PDF to Markdown with LLM assist."""

    DEFAULT_MODELS = ["gpt-4o", "qwen2.5:14b"]

    def __init__(
        self,
        ollama_endpoint: str = "http://localhost:11434/v1",
        ollama_model: str = "qwen2.5:14b",
        use_llm_assist: bool = True,
    ):
        """Initialize PDF processor.

        Args:
            ollama_endpoint: Ollama API endpoint
            ollama_model: Model to use for LLM assist
            use_llm_assist: Whether to use LLM for table/figure extraction
        """
        if not HAS_MARKER:
            raise ImportError(
                "marker-pdf not installed. Install with: pip install marker-pdf"
            )

        self.ollama_endpoint = ollama_endpoint
        self.ollama_model = ollama_model
        self.use_llm_assist = use_llm_assist

        self._markdown_pattern = re.compile(r"^{%.*%}$", re.MULTILINE)

    def convert_to_markdown(
        self,
        pdf_path: str,
        output_dir: Optional[str] = None,
    ) -> str:
        """Convert PDF to Markdown.

        Args:
            pdf_path: Path to PDF file
            output_dir: Optional directory to save Markdown

        Returns:
            Markdown content as string
        """
        path = Path(pdf_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        # Use Marker to convert PDF
        full_typst, document = convert_single_pdf(
            str(path),
            llm_mode="full" if self.use_llm_assist else "simple",
        )

        # Convert to markdown
        markdown = convert_document_to_markdown(document)

        # Clean up markdown
        markdown = self._clean_md(markdown)

        # Save if output_dir provided
        if output_dir:
            output_path = Path(output_dir) / f"{path.stem}.md"
            output_path.write_text(markdown, encoding="utf-8")

        return markdown

    def _clean_md(self, markdown: str) -> str:
        """Clean up Markdown output."""
        # Remove typst markers
        markdown = self._markdown_pattern.sub("", markdown)

        # Clean up excessive whitespace
        markdown = re.sub(r"\n\n\n+", "\n\n", markdown)

        # Remove leading/trailing whitespace
        markdown = markdown.strip()

        return markdown

    def chunk_by_sections(
        self,
        markdown: str,
        max_chunk_size: int = 4000,
    ) -> list[dict]:
        """Chunk markdown by sections.

        Args:
            markdown: Markdown content
            max_chunk_size: Maximum chunk size in characters

        Returns:
            List of dicts with 'text', 'section', 'start_char', 'end_char'
        """
        sections = self._split_into_sections(markdown)
        chunks = []

        current_chunk: list[str] = []
        current_size = 0

        for section in sections:
            section_text = section["text"]
            section_size = len(section_text)

            if current_size + section_size > max_chunk_size:
                if current_chunk:
                    chunks.append(
                        {
                            "text": "\n\n".join(current_chunk),
                            "section": "combined",
                            "start_char": sections[0]["start_char"],
                            "end_char": section["start_char"],
                        }
                    )
                current_chunk = [section_text]
                current_size = section_size
            else:
                current_chunk.append(section_text)
                current_size += section_size

        if current_chunk:
            chunks.append(
                {
                    "text": "\n\n".join(current_chunk),
                    "section": (
                        "combined"
                        if len(current_chunk) > 1
                        else sections[-1]["section"]
                    ),
                    "start_char": sections[0]["start_char"],
                    "end_char": sections[-1]["end_char"],
                }
            )

        return chunks

    def _split_into_sections(self, markdown: str) -> list[dict]:
        """Split markdown into logical sections."""
        sections: list[dict] = []
        current_section: list[str] = []
        current_label = "body"

        # Section headers (Markdown or Typst style)
        section_pattern = re.compile(
            r"^(#+\s+|^\s*%section\s+)(?P<title>.+?)$", re.MULTILINE
        )

        lines = markdown.split("\n")

        for i, line in enumerate(lines):
            match = section_pattern.match(line)
            if match:
                # Save previous section
                if current_section:
                    sections.append(
                        {
                            "text": "\n".join(current_section),
                            "section": current_label,
                            "start_char": 0,
                            "end_char": 0,
                            "title": match.group("title").strip(),
                        }
                    )

                # Start new section
                current_label = match.group("title").strip().lower()
                current_section = [line]
            else:
                current_section.append(line)

        # Save last section
        if current_section:
            sections.append(
                {
                    "text": "\n".join(current_section),
                    "section": current_label,
                    "start_char": 0,
                    "end_char": 0,
                    "title": current_label,
                }
            )

        return sections
