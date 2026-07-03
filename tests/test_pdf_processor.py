from pathlib import Path

from src.chunker import Chunker
from src.pdf_processor import PDFProcessor


def test_lightweight_pdf_extraction_uses_embedded_text_layer():
    pdf = Path(__file__).parent.parent / "facets_test_set" / "pdf" / "DKXM2EP7.pdf"
    markdown = PDFProcessor().convert_to_markdown(str(pdf))
    assert markdown.startswith("## Page 1")
    assert "Vegetation Cover" in markdown
    assert 10_000 < len(markdown) < 100_000


def test_page_headings_are_preserved_as_chunk_metadata():
    chunks = Chunker(max_characters=1000, max_chunk_size=1000).chunk_text(
        "## Page 1\nFirst page sentence.\n\n## Page 2\nSecond page sentence."
    )
    assert [chunk.page for chunk in chunks] == [1, 2]


def test_character_limit_is_not_overridden_by_sentence_count():
    text = " ".join(f"Sentence {number}." for number in range(200))
    chunks = Chunker(
        max_characters=40_000,
        max_chunk_size=40_000,
        max_sentences=None,
    ).chunk_text(text)
    assert len(chunks) == 1


def test_disabled_limits_use_one_whole_document_chunk():
    text = "## Page 1\nFirst page.\n\n## Page 2\nSecond page."
    chunks = Chunker(
        max_characters=None,
        max_chunk_size=None,
        max_sentences=None,
    ).chunk_text(text)
    assert len(chunks) == 1
    assert chunks[0].text == text
    assert chunks[0].section == "document"
