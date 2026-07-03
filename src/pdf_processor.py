"""Lightweight PDF-to-Markdown conversion using pypdf."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from pypdf import PdfReader
from pypdf.errors import PdfReadError


class PDFProcessor:
    """Extract the embedded PDF text layer without OCR or model downloads.

    This deliberately small temporary engine works well for born-digital PDFs.
    It cannot recover text from scanned/image-only documents.
    """

    def __init__(self):
        self.last_warnings: list[str] = []

    def convert_to_markdown(
        self, pdf_path: str, output_dir: Optional[str] = None
    ) -> str:
        path = Path(pdf_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        try:
            reader = PdfReader(str(path))
            if reader.is_encrypted and not reader.decrypt(""):
                raise RuntimeError(f"PDF is encrypted and cannot be read: {pdf_path}")
            pages = [
                self._extract_page(page, number)
                for number, page in enumerate(reader.pages, 1)
            ]
        except PdfReadError as exc:
            raise RuntimeError(f"Could not parse PDF {pdf_path}: {exc}") from exc

        extracted_pages = [page for page in pages if page[1]]
        if not extracted_pages:
            raise RuntimeError(
                "The PDF contains no extractable text layer. It is probably scanned "
                "and requires an OCR engine."
            )

        markdown_parts = []
        for page_number, text in pages:
            markdown_parts.append(f"## Page {page_number}")
            if text:
                markdown_parts.append(text)
            else:
                self.last_warnings.append(f"Page {page_number} has no extractable text")
        markdown = "\n\n".join(markdown_parts).strip()

        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            (output_path / f"{path.stem}.md").write_text(markdown, encoding="utf-8")
        return markdown

    @staticmethod
    def _extract_page(page, page_number: int) -> tuple[int, str]:
        # Plain extraction avoids the large runs of layout-padding spaces that
        # dramatically inflate context size on multi-column journal articles.
        text = page.extract_text() or ""
        text = text.replace("\x00", "")
        text = "\n".join(line.rstrip() for line in text.splitlines())
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return page_number, text
