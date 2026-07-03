"""RIS file reader for article metadata."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
from urllib.parse import unquote, urlparse


@dataclass
class ArticleMetadata:
    """Metadata extracted from RIS file."""

    entry_type: Optional[str] = None
    title: Optional[str] = None
    authors: list = field(default_factory=list)
    year: Optional[str] = None
    journal: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    abstract: Optional[str] = None
    keywords: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    source_file: Optional[str] = None
    record_id: Optional[str] = None
    attachment_path: Optional[str] = None


class RISReader:
    """Reader for RIS (Research Information System) files."""

    RIS_TAGS = {
        "TY": "entry_type",
        "ID": "record_id",
        "TI": "title",
        "AU": "authors",
        "PY": "year",
        "JO": "journal",
        "VL": "volume",
        "IS": "issue",
        "SP": "pages",
        "DO": "doi",
        "UR": "url",
        "AB": "abstract",
        "KW": "keywords",
        "N1": "notes",
        "L1": "attachment_path",
        "ER": "end_record",
    }

    def __init__(self):
        """Initialize RIS reader."""
        self._tag_pattern = re.compile(r"^(?P<tag>\w{2})  -\s*(?P<content>.*)$")

    def read_file(self, file_path: str) -> list[ArticleMetadata]:
        """Read RIS file and extract article metadata.

        Args:
            file_path: Path to RIS file

        Returns:
            List of ArticleMetadata objects (one per entry)
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"RIS file not found: {file_path}")

        entries: list[ArticleMetadata] = []
        current_entry: dict[str, Any] = {}

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                match = self._tag_pattern.match(line)
                if match:
                    tag = match.group("tag")
                    content = match.group("content").strip()

                    if tag == "ER":
                        if current_entry:
                            entries.append(
                                self._create_article_metadata(current_entry, str(path))
                            )
                            current_entry = {}
                    elif tag in self.RIS_TAGS:
                        field_name = self.RIS_TAGS[tag]
                        self._add_field(current_entry, field_name, content)

            # Handle last entry if file doesn't end with ER
            if current_entry:
                entries.append(self._create_article_metadata(current_entry, str(path)))

        return entries

    def read_string(self, ris_content: str) -> list[ArticleMetadata]:
        """Parse RIS content from string.

        Args:
            ris_content: String containing RIS-formatted data

        Returns:
            List of ArticleMetadata objects
        """
        entries: list[ArticleMetadata] = []
        current_entry: dict[str, Any] = {}

        for line in ris_content.splitlines():
            line = line.strip()
            if not line:
                continue

            match = self._tag_pattern.match(line)
            if match:
                tag = match.group("tag")
                content = match.group("content").strip()

                if tag == "ER":
                    if current_entry:
                        entries.append(self._create_article_metadata(current_entry, ""))
                        current_entry = {}
                elif tag in self.RIS_TAGS:
                    field_name = self.RIS_TAGS[tag]
                    self._add_field(current_entry, field_name, content)

        if current_entry:
            entries.append(self._create_article_metadata(current_entry, ""))

        return entries

    def _add_field(self, entry: dict, field_name: str, content: str) -> None:
        """Add field to entry, handling multi-valued fields."""
        if field_name == "authors":
            if field_name not in entry:
                entry[field_name] = []
            entry[field_name].append(content)
        elif field_name == "keywords":
            if field_name not in entry:
                entry[field_name] = []
            # Keywords may be comma-separated
            for kw in content.split(","):
                kw = kw.strip()
                if kw:
                    entry[field_name].append(kw)
        elif field_name == "notes":
            if field_name not in entry:
                entry[field_name] = []
            entry[field_name].append(content)
        else:
            entry[field_name] = content

    def _create_article_metadata(
        self, entry: dict, source_file: str
    ) -> ArticleMetadata:
        """Create ArticleMetadata object from entry dict."""
        return ArticleMetadata(
            entry_type=entry.get("entry_type"),
            title=entry.get("title"),
            authors=entry.get("authors", []),
            year=entry.get("year"),
            journal=entry.get("journal"),
            volume=entry.get("volume"),
            issue=entry.get("issue"),
            pages=entry.get("pages"),
            doi=entry.get("doi"),
            url=entry.get("url"),
            abstract=entry.get("abstract"),
            keywords=entry.get("keywords", []),
            notes=entry.get("notes", []),
            source_file=source_file,
            record_id=entry.get("record_id"),
            attachment_path=self._normalize_attachment(entry.get("attachment_path")),
        )

    @staticmethod
    def _normalize_attachment(value: Optional[str]) -> Optional[str]:
        if not value:
            return None
        if value.startswith("file:"):
            parsed = urlparse(value)
            path = unquote(parsed.path)
            if re.match(r"^/[A-Za-z]:/", path):
                path = path[1:]
            return path
        return unquote(value)
