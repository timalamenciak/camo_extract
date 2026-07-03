import json
from pathlib import Path

import yaml

from src.config import load_config
from src.consolidator import Consolidator
from src.main import process_folder
from src.ontology_grounder import GroundingDecision, OntologyCandidate
from src.schema_validation import normalize_graph, validate_graph

RAW_GRAPH = {
    "nodes": [
        {
            "id": "cause",
            "name": "Supplemental seeding",
            "entity_type": "management_intervention",
            "entity_mention": "supplemental seeding",
            "state_or_change_qualifier": "occurred",
            "source_spans": [
                {"text": "Supplemental seeding increased native richness."}
            ],
        },
        {
            "id": "effect",
            "name": "Increased native richness",
            "entity_type": "environmental_variable",
            "entity_mention": "native plant community",
            "measured_attribute_mention": "native species richness",
            "state_or_change_qualifier": "increased",
            "source_spans": [
                {"text": "Supplemental seeding increased native richness."}
            ],
        },
    ],
    "edges": [
        {
            "id": "claim",
            "subject": "cause",
            "predicate": "causes",
            "object": "effect",
            "claim_strength": "direct_causal",
            "philosophical_accounts": ["interventionist"],
            "original_sentence": "Supplemental seeding increased native richness.",
            "evidential_basis": {
                "evidence_types": ["randomized_experiment"],
                "evidence_objects": ["correlation"],
            },
        }
    ],
}


class FakeExtractor:
    def extract(self, text, metadata):
        return json.loads(json.dumps(RAW_GRAPH))


class FakeGrounder:
    def ground_node(self, node):
        node = dict(node)
        mention = node.pop("entity_mention")
        attribute = node.pop("measured_attribute_mention", None)
        if node["entity_type"] == "management_intervention":
            candidate = OntologyCandidate(
                "ELMO:3620500", "supplemental seeding", "ELMO"
            )
            decision = GroundingDecision(
                mention, node["entity_type"], "exact_match", ["ELMO"], candidate
            )
            node["entity_term"] = candidate.curie
            decisions = [decision]
        else:
            decision = GroundingDecision(
                mention, node["entity_type"], "no_match", ["ELMO", "ENVO"]
            )
            node["entity_term"] = "causal_mosaic:unresolved_test"
            decisions = [decision]
        if attribute:
            node["measured_attribute"] = attribute
            decisions.append(
                GroundingDecision(attribute, "variable", "no_match", ["ELMO", "PATO"])
            )
        return node, decisions


class FakePDFProcessor:
    def convert_to_markdown(self, path):
        return "# Results\nSupplemental seeding increased native richness."


def test_normalized_graph_validates_and_has_resolved_edges():
    graph = json.loads(json.dumps(RAW_GRAPH))
    graph["nodes"][0]["entity_term"] = "ELMO:3620500"
    graph["nodes"][1]["entity_term"] = "ENVO:01001206"
    normalized = normalize_graph(
        graph, {"doi": "10.1/test", "title": "Test", "year": 2024}
    )
    validate_graph(normalized)
    ids = {node["id"] for node in normalized["nodes"]}
    assert normalized["edges"][0]["subject"] in ids
    assert normalized["edges"][0]["object"] in ids


def test_consolidator_preserves_reference_integrity():
    graph = json.loads(json.dumps(RAW_GRAPH))
    graph["nodes"][0]["entity_term"] = "ELMO:3620500"
    graph["nodes"][1]["entity_term"] = "ENVO:01001206"
    normalized = normalize_graph(graph, {"doi": "10.1/test", "title": "Test"})
    consolidated = Consolidator().consolidate([normalized, normalized])
    validate_graph(consolidated)
    assert len(consolidated["nodes"]) == 2
    assert len(consolidated["edges"]) == 1


def test_mediator_references_are_remapped():
    graph = json.loads(json.dumps(RAW_GRAPH))
    graph["nodes"].append(
        {
            "id": "mediator",
            "name": "Nutrient cycling",
            "entity_type": "environmental_process",
            "entity_term": "ENVO:02500010",
            "state_or_change_qualifier": "occurred",
        }
    )
    graph["nodes"][0]["entity_term"] = "ELMO:3620500"
    graph["nodes"][1]["entity_term"] = "ENVO:01001206"
    graph["edges"][0]["mediation"] = {
        "status": "explicitly_asserted",
        "mediator_node_ids": ["mediator"],
    }
    normalized = normalize_graph(graph, {"doi": "10.1/mediation", "title": "Test"})
    consolidated = Consolidator().consolidate([normalized])
    validate_graph(consolidated)
    ids = {node["id"] for node in consolidated["nodes"]}
    assert consolidated["edges"][0]["mediation"]["mediator_node_ids"][0] in ids


def test_end_to_end_writes_equivalent_graphs_and_gap_report(tmp_path: Path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    (input_dir / "ABC123.pdf").write_bytes(b"not read by fake processor")
    (input_dir / "articles.ris").write_text(
        "TY  - JOUR\nID  - ABC123\nTI  - Test article\nPY  - 2024\n"
        "DO  - 10.1/test\nL1  - file:///old/ABC123.pdf\nER  -\n",
        encoding="utf-8",
    )
    manifest = process_folder(
        str(input_dir),
        str(output_dir),
        config=load_config(),
        extractor=FakeExtractor(),
        grounder=FakeGrounder(),
        pdf_processor=FakePDFProcessor(),
    )
    assert len(manifest["processed"]) == 1
    json_graph = json.loads(
        (output_dir / "causal_graph.json").read_text(encoding="utf-8")
    )
    yaml_graph = yaml.safe_load(
        (output_dir / "causal_graph.yaml").read_text(encoding="utf-8")
    )
    assert json_graph == yaml_graph
    validate_graph(json_graph)
    gaps = yaml.safe_load(
        (output_dir / "ontology_gaps.yaml").read_text(encoding="utf-8")
    )
    assert {gap["semantic_role"] for gap in gaps["gaps"]} == {
        "environmental_variable",
        "variable",
    }
    assert (output_dir / "ontology_gaps.csv").exists()
    assert not manifest["failed"]
