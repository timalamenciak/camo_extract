"""Text chunker for context window management."""

import re
from typing import Optional
from dataclasses import dataclass


@dataclass
class Chunk:
    """A text chunk with metadata."""

    text: str
    start_char: int
    end_char: int
    section: str = "unknown"
    page: Optional[int] = None
    line_range: Optional[tuple[int, int]] = None
    token_count: Optional[int] = None


class Chunker:
    """Chunk text for context window limitations."""

    DEFAULT_SECTION_HEADINGS = [
        r"^#+\s+",
        r"^\s*%section\s+",
    ]

    def __init__(
        self,
        max_chunk_size: int = 8000,
        overlap_size: int = 400,
        max_sentences: int = 10,
        max_characters: int = 4000,
    ):
        """Initialize chunker.

        Args:
            max_chunk_size: Maximum chunk size in characters
            overlap_size: Overlap between chunks
            max_sentences: Max sentences per chunk
            max_characters: Max characters per chunk
        """
        self.max_chunk_size = max_chunk_size
        self.overlap_size = overlap_size
        self.max_sentences = max_sentences
        self.max_characters = max_characters

    def chunk_text(
        self,
        text: str,
        section: str = "unknown",
        page: Optional[int] = None,
    ) -> list[Chunk]:
        """Chunk text into context-window-sized pieces.

        Args:
            text: Text to chunk
            section: Section name (for metadata)
            page: Page number (for metadata)

        Returns:
            List of Chunk objects
        """
        if not text or not text.strip():
            return []

        # First split by section heads
        section_chunks = self._split_by_sections(text, section, page)

        # Then chunk each section
        all_chunks = []
        for section_chunk in section_chunks:
            chunks = self._chunk_section(
                section_chunk.text, section_chunk.section, page
            )
            for chunk in chunks:
                chunk.start_char += section_chunk.start_char
                chunk.end_char += section_chunk.start_char
            all_chunks.extend(chunks)

        return all_chunks

    def _split_by_sections(
        self, text: str, default_section: str, page: Optional[int]
    ) -> list[Chunk]:
        """Split text into sections."""
        sections: list[Chunk] = []

        # Try to find section headers
        current_section: list[str] = []
        current_label = default_section

        lines = text.split("\n")

        for line in lines:
            if self._is_section_header(line):
                if current_section:
                    sections.append(
                        Chunk(
                            text="\n".join(current_section),
                            start_char=0,
                            end_char=0,
                            section=current_label,
                            page=page,
                        )
                    )
                current_label = self._extract_section_name(line)
                current_section = [line]
            else:
                current_section.append(line)

        if current_section:
            sections.append(
                Chunk(
                    text="\n".join(current_section),
                    start_char=0,
                    end_char=0,
                    section=current_label,
                    page=page,
                )
            )

        return sections

    def _chunk_section(
        self, text: str, section: str, page: Optional[int]
    ) -> list[Chunk]:
        """Chunk a section into smaller pieces."""
        chunks: list[Chunk] = []

        # Split into sentences
        sentences = self._split_into_sentences(text)

        current_chunk: list[str] = []
        current_size = 0

        for sentence in sentences:
            sentence_size = len(sentence)

            if current_size + sentence_size > self.max_characters:
                if current_chunk:
                    chunks.append(self._create_chunk(current_chunk, section, page))
                current_chunk = [sentence]
                current_size = sentence_size
            else:
                current_chunk.append(sentence)
                current_size += sentence_size

        if current_chunk:
            chunks.append(self._create_chunk(current_chunk, section, page))

        # Apply overlap if configured
        if self.overlap_size > 0 and len(chunks) > 1:
            chunks = self._apply_overlap(chunks)

        return chunks

    def _create_chunk(
        self, sentences: list[str], section: str, page: Optional[int]
    ) -> Chunk:
        """Create a Chunk from sentences."""
        text = " ".join(sentences)
        return Chunk(
            text=text,
            start_char=0,
            end_char=len(text),
            section=section,
            page=page,
            line_range=None,
            token_count=None,
        )

    def _apply_overlap(self, chunks: list[Chunk]) -> list[Chunk]:
        """Apply overlap between chunks."""
        overlapped: list[Chunk] = []

        for i, chunk in enumerate(chunks):
            if i > 0:
                # Add overlap from previous chunk
                prev_text = overlapped[-1].text
                overlap_start = max(0, len(prev_text) - self.overlap_size)
                overlap_text = prev_text[overlap_start:]
                chunk.text = overlap_text + "\n" + chunk.text
                chunk.start_char -= len(overlap_text)

            overlapped.append(chunk)

        return overlapped

    def _split_into_sentences(self, text: str) -> list[str]:
        """Split text into sentences."""
        # Simple sentence splitting
        sentences = re.split(r"(?<=[.!?])\s+", text)

        # Clean up
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def _is_section_header(self, line: str) -> bool:
        """Check if line is a section header."""
        patterns = [
            r"^#+\s+",
            r"^\s*%section\s+",
        ]

        for pattern in patterns:
            if re.match(pattern, line):
                return True

        return False

    def _extract_section_name(self, line: str) -> str:
        """Extract section name from header line."""
        # Remove markdown headers
        name = re.sub(r"^#+\s+", "", line)
        name = re.sub(r"^\s*%section\s+", "", name)
        return name.strip().lower()
