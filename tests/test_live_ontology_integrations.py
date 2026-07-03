import os

import pytest

from src.config import load_config
from src.ontology_grounder import ELMOClient, OLSClient, WikidataClient

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
        os.environ.get("RUN_LIVE_ONTOLOGY_TESTS") != "1",
        reason="Set RUN_LIVE_ONTOLOGY_TESTS=1 to call OLS, ELMO, and Wikidata",
    ),
]


@pytest.fixture(scope="module")
def ontology_config():
    return load_config().ontology


def test_ols_envo_integration(ontology_config):
    results = OLSClient(
        ontology_config.ols_endpoint, ontology_config.request_timeout
    ).search("grassland ecosystem", "ENVO")
    assert any(
        item.ontology == "ENVO" and "grassland" in item.label.casefold()
        for item in results
    )


def test_elmo_integration(ontology_config):
    results = ELMOClient(
        ontology_config.elmo_url, ontology_config.request_timeout
    ).search("tree planting process")
    assert any(
        item.ontology == "ELMO" and item.label.casefold() == "tree planting process"
        for item in results
    )


def test_wikidata_taxon_integration(ontology_config):
    results = WikidataClient(
        ontology_config.wikidata_endpoint, ontology_config.request_timeout
    ).search("Canis lupus")
    assert any(item.curie == "WD:Q18498" for item in results)
