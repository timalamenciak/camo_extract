"""Normalization and LinkML-backed validation for CAMO graphs."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import jsonschema
from linkml.generators.jsonschemagen import JsonSchemaGenerator

SCHEMA_PATH = Path(__file__).parent.parent / "causal_mosaic_v0.7.1.yaml"


def stable_id(prefix: str, *parts: object) -> str:
    material = "|".join(str(part) for part in parts)
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}:{digest}"


def normalize_graph(graph: dict, source: dict | None = None) -> dict:
    """Convert extraction drafts and legacy output into CAMO v0.7.1 shape."""
    source = source or {}
    nodes = []
    id_map: dict[str, str] = {}
    for index, raw in enumerate(graph.get("nodes", [])):
        node = dict(raw)
        old_id = str(node.get("id") or f"draft_node_{index}")
        node_id = stable_id(
            "causal_mosaic:node",
            source.get("doi", ""),
            node.get("entity_term") or node.get("entity_mention") or node.get("entity"),
            node.get("measured_attribute") or node.get("attribute"),
            node.get("state_or_change_qualifier") or node.get("state_qualifier"),
        )
        id_map[old_id] = node_id
        normalized = {
            "id": node_id,
            "name": node.get("name")
            or node.get("entity_label")
            or node.get("entity_mention")
            or "Unnamed ecological entity",
            "entity_type": node.get("entity_type", "environmental_variable"),
            "entity_term": node.get("entity_term")
            or node.get("entity")
            or node.get("entity_mention")
            or "causal_mosaic:unresolved",
            "state_or_change_qualifier": node.get("state_or_change_qualifier")
            or node.get("state_qualifier")
            or "unspecified",
        }
        measured = node.get("measured_attribute") or node.get("attribute")
        if measured:
            normalized["measured_attribute"] = measured
        spans = node.get("source_spans")
        if spans:
            normalized["source_spans"] = spans
        nodes.append(normalized)

    edges = []
    for index, raw in enumerate(graph.get("edges", [])):
        edge = dict(raw)
        subject = str(edge.get("subject") or edge.get("subject_node_id") or "")
        object_ = str(edge.get("object") or edge.get("object_node_id") or "")
        evidence = edge.get("evidential_basis") or edge.get("evidence") or {}
        accounts = (
            edge.get("philosophical_accounts")
            or edge.get("philosophical_account")
            or ["probabilistic"]
        )
        if isinstance(accounts, str):
            accounts = [accounts]
        original_sentence = edge.get("original_sentence") or edge.get("prov", {}).get(
            "source_text", ""
        )
        normalized = {
            "id": stable_id(
                "causal_mosaic:edge",
                source.get("doi", ""),
                subject,
                object_,
                edge.get("predicate"),
                original_sentence,
                index,
            ),
            "subject": id_map.get(subject, subject),
            "predicate": edge.get("predicate", "associated_with"),
            "object": id_map.get(object_, object_),
            "claim_strength": edge.get("claim_strength", "associational"),
            "philosophical_accounts": accounts,
            "original_sentence": original_sentence,
            "source_spans": edge.get("source_spans") or [{"text": original_sentence}],
            "evidential_basis": {
                "evidence_types": _as_list(
                    evidence.get("evidence_types")
                    or evidence.get("evidence_type")
                    or evidence.get("type")
                    or "observational_cross_sectional"
                ),
                "evidence_objects": _as_list(
                    evidence.get("evidence_objects")
                    or evidence.get("evidence_object")
                    or evidence.get("object")
                    or "correlation"
                ),
            },
            "source_document": {
                key: value
                for key, value in {
                    "doi": source.get("doi"),
                    "title": source.get("title"),
                    "year": _integer_or_none(source.get("year")),
                    "authors": source.get("authors"),
                    "journal": source.get("journal"),
                }.items()
                if value not in (None, "", [])
            },
        }
        for feature in (
            "necessity",
            "sufficiency",
            "temporal_ordering",
            "specificity",
            "stability",
            "token_or_type",
            "determinism",
            "proximate_distal",
            "contributing_sole",
            "reversibility",
            "proportionality",
        ):
            value = edge.get(feature) or edge.get("features", {}).get(feature)
            if value:
                normalized[feature] = value
        for structure in (
            "direction",
            "mediation",
            "moderation",
            "strength",
            "context_dependence",
            "temporal_extent",
        ):
            if edge.get(structure):
                normalized[structure] = edge[structure]
        for structure, field in (
            ("mediation", "mediator_node_ids"),
            ("moderation", "moderator_node_ids"),
        ):
            if structure in normalized and field in normalized[structure]:
                normalized[structure][field] = [
                    id_map.get(reference, reference)
                    for reference in normalized[structure][field]
                ]
        edges.append(normalized)

    graph_id = graph.get("graph_id") or stable_id(
        "causal_mosaic:graph", source.get("doi") or source.get("title") or "corpus"
    )
    return {
        "graph_id": graph_id,
        "schema_version": "0.7.1",
        "provenance": {
            "ontology_framework": "ELMO + ENVO + Wikidata + CAMO",
            "elm_version": "2026-07-03",
            "causal_mosaic_version": "0.7.1",
            "created": datetime.now(timezone.utc).isoformat(),
            "source_corpus": source.get("title")
            or graph.get("provenance", {}).get(
                "source_corpus", "Scientific literature corpus"
            ),
            "project": "EcoWeaver",
        },
        "nodes": nodes,
        "edges": edges,
    }


def validate_graph(graph: dict) -> None:
    """Raise jsonschema.ValidationError when a graph violates CAMO."""
    _validator().validate(graph)
    node_ids = {node["id"] for node in graph.get("nodes", [])}
    for edge in graph.get("edges", []):
        if edge.get("subject") not in node_ids or edge.get("object") not in node_ids:
            raise ValueError(f"Dangling node reference in edge {edge.get('id')}")
        nested_references = [
            *edge.get("mediation", {}).get("mediator_node_ids", []),
            *edge.get("moderation", {}).get("moderator_node_ids", []),
        ]
        if any(reference not in node_ids for reference in nested_references):
            raise ValueError(
                f"Dangling mediator/moderator reference in edge {edge.get('id')}"
            )


@lru_cache(maxsize=1)
def _validator():
    schema = json.loads(
        JsonSchemaGenerator(str(SCHEMA_PATH), top_class="CausalGraph").serialize()
    )
    return jsonschema.Draft7Validator(schema)


def _integer_or_none(value):
    try:
        return int(str(value)[:4]) if value else None
    except (TypeError, ValueError):
        return None


def _as_list(value):
    return value if isinstance(value, list) else [value]
