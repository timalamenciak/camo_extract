from pathlib import Path

from src.config import load_config
from src.main import _find_pdf_for_article
from src.ontology_grounder import OntologyCandidate, _candidate_score
from src.risc_reader import ArticleMetadata, RISReader


def test_ris_attachment_and_record_id_are_parsed():
    article = RISReader().read_string(
        "TY  - JOUR\nID  - A1B2\nTI  - Example\nL1  - file:///C:/old/A1B2.pdf\nER  -\n"
    )[0]
    assert article.record_id == "A1B2"
    assert article.attachment_path.endswith("A1B2.pdf")


def test_pdf_matching_never_falls_back_to_first_file(tmp_path: Path):
    first = tmp_path / "first.pdf"
    expected = tmp_path / "RECORD9.pdf"
    first.touch()
    expected.touch()
    assert (
        _find_pdf_for_article(ArticleMetadata(record_id="RECORD9"), [first, expected])
        == expected
    )
    assert (
        _find_pdf_for_article(
            ArticleMetadata(doi="10.1234/not-present"), [first, expected]
        )
        is None
    )


def test_candidate_acceptance_is_conservative():
    exact = OntologyCandidate("PATO:1", "abundance", "PATO")
    unrelated = OntologyCandidate(
        "MSIO:1", "mass isotopomer fractional abundance", "MSIO"
    )
    assert _candidate_score("abundance", exact) == 1.0
    assert exact.match_type == "exact_match"
    assert _candidate_score("abundance", unrelated) < 0.9
    assert unrelated.match_type == "close_match_needs_review"


def test_environment_placeholders_are_expanded():
    config = load_config()
    assert not (config.llm.api_key or "").startswith("${")


def test_facets_manifest_maps_records_to_their_named_pdfs():
    root = Path(__file__).parent.parent / "facets_test_set" / "pdf"
    articles = RISReader().read_file(str(root / "pdfs_manifest.ris"))
    pdfs = list(root.glob("*.pdf"))
    assert len(articles) > 100
    matched = [_find_pdf_for_article(article, pdfs) for article in articles]
    assert sum(item is not None for item in matched) >= int(len(articles) * 0.95)
    for article, pdf in zip(articles[:25], matched[:25]):
        assert pdf is not None
        assert pdf.stem.casefold() == article.record_id.casefold()
