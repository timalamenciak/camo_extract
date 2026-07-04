"""Normalization and LinkML-backed validation for CAMO graphs."""

from __future__ import annotations

import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import jsonschema
from linkml.generators.jsonschemagen import JsonSchemaGenerator

SCHEMA_PATH = Path(__file__).parent.parent / "causal_mosaic_v0.7.1.yaml"
LOGGER = logging.getLogger("camo_extract")

STATE_VALUES = {
    "increased",
    "decreased",
    "present",
    "absent",
    "introduced",
    "removed",
    "unchanged",
    "unspecified",
    "occurred",
    "initiated",
    "terminated",
    "ongoing",
    "interrupted",
    "aborted",
}
STATE_ALIASES = {
    "increase": "increased",
    "elevated": "increased",
    "higher": "increased",
    "enhanced": "increased",
    "improved": "increased",
    "recovered": "increased",
    "reduced": "decreased",
    "reduction": "decreased",
    "declined": "decreased",
    "declining": "decreased",
    "lower": "decreased",
    "lowered": "decreased",
    "stable": "unchanged",
    "maintained": "unchanged",
    "no_change": "unchanged",
    "established": "present",
    "colonized": "present",
    "lost": "absent",
    "eliminated": "absent",
    "started": "initiated",
    "ended": "terminated",
    "stopped": "terminated",
    "continuing": "ongoing",
    "unknown": "unspecified",
}
ENTITY_VALUES = {
    "environmental_variable",
    "environmental_process",
    "management_intervention",
    "taxon",
}
ENTITY_ALIASES = {
    "variable": "environmental_variable",
    "environmental_factor": "environmental_variable",
    "process": "environmental_process",
    "management_process": "management_intervention",
    "intervention": "management_intervention",
    "management_action": "management_intervention",
    "species": "taxon",
    "taxa": "taxon",
    "organism": "taxon",
}
PREDICATE_VALUES = {
    "causes",
    "contributes_to",
    "associated_with",
    "prevents",
    "enables",
    "disrupts",
    "regulates",
    "positively_regulates",
    "negatively_regulates",
    "mediates",
    "moderates",
    "precedes",
    "correlated_with",
}
PREDICATE_ALIASES = {
    "leads_to": "causes",
    "results_in": "causes",
    "affects": "regulates",
    "increases": "positively_regulates",
    "promotes": "positively_regulates",
    "decreases": "negatively_regulates",
    "reduces": "negatively_regulates",
    "inhibits": "prevents",
    "facilitates": "enables",
    "correlates_with": "correlated_with",
    "is_associated_with": "associated_with",
}
CLAIM_VALUES = {"no_relationship", "associational", "uncertain_causal", "direct_causal"}
CLAIM_ALIASES = {
    "correlation": "associational",
    "correlational": "associational",
    "association": "associational",
    "uncertain": "uncertain_causal",
    "causal": "direct_causal",
    "direct": "direct_causal",
    "none": "no_relationship",
}
ACCOUNT_VALUES = {
    "counterfactual",
    "probabilistic",
    "interventionist",
    "transmission",
    "mechanistic",
    "regularity",
    "inus_component",
    "agency",
}
ACCOUNT_ALIASES = {
    "intervention": "interventionist",
    "mechanism": "mechanistic",
    "difference_making": "probabilistic",
    "inus": "inus_component",
}
FEATURE_VALUES = {
    "explicitly_asserted",
    "implicitly_assumed",
    "explicitly_denied",
    "not_addressed",
}
FEATURE_ALIASES = {
    "yes": "explicitly_asserted",
    "true": "explicitly_asserted",
    "asserted": "explicitly_asserted",
    "present": "explicitly_asserted",
    "implicit": "implicitly_assumed",
    "implied": "implicitly_assumed",
    "no": "explicitly_denied",
    "false": "explicitly_denied",
    "denied": "explicitly_denied",
    "absent": "explicitly_denied",
    "unknown": "not_addressed",
    "unspecified": "not_addressed",
    "ambiguous": "not_addressed",
    "not_specified": "not_addressed",
}
TOKEN_VALUES = {"token", "type", "ambiguous", "not_addressed"}
TOKEN_ALIASES = {"instance": "token", "general": "type", "unknown": "ambiguous"}
DETERMINISM_VALUES = {
    "deterministic_process",
    "indeterministic_process",
    "epistemic_probability_only",
    "ambiguous",
    "not_addressed",
}
DETERMINISM_ALIASES = {
    "deterministic": "deterministic_process",
    "indeterministic": "indeterministic_process",
    "probabilistic": "indeterministic_process",
    "epistemic": "epistemic_probability_only",
    "unknown": "ambiguous",
}
PROXIMATE_VALUES = {"proximate", "distal", "both_specified", "not_addressed"}
PROXIMATE_ALIASES = {"both": "both_specified", "unknown": "not_addressed"}
CONTRIBUTING_VALUES = {"sole_cause", "contributing_cause", "not_addressed"}
CONTRIBUTING_ALIASES = {
    "sole": "sole_cause",
    "contributing": "contributing_cause",
    "multiple": "contributing_cause",
    "unknown": "not_addressed",
}
REVERSIBILITY_VALUES = {
    "reversible",
    "irreversible",
    "partially_reversible",
    "hysteresis",
    "not_addressed",
}
REVERSIBILITY_ALIASES = {
    "partial": "partially_reversible",
    "partialy_reversible": "partially_reversible",
    "unknown": "not_addressed",
}
DIRECTION_STATUS_VALUES = {"asserted", "uncertain", "bidirectional", "not_addressed"}
DIRECTION_STATUS_ALIASES = {
    "explicit": "asserted",
    "unidirectional": "asserted",
    "unknown": "not_addressed",
}
DIRECTION_EVIDENCE_VALUES = {
    "experimental",
    "temporal_precedence",
    "theoretical",
    "natural_experiment",
    "structural_model",
}
DIRECTION_EVIDENCE_ALIASES = {
    "temporal": "temporal_precedence",
    "experiment": "experimental",
    "model": "structural_model",
    "sem": "structural_model",
}
INTERACTION_VALUES = {
    "synergistic",
    "antagonistic",
    "qualitative",
    "quantitative",
    "not_specified",
}
INTERACTION_ALIASES = {"unknown": "not_specified", "unspecified": "not_specified"}
STRENGTH_VALUES = {"strong", "moderate", "weak", "negligible", "not_specified"}
STRENGTH_ALIASES = {
    "high": "strong",
    "medium": "moderate",
    "low": "weak",
    "unknown": "not_specified",
}
EVIDENCE_TYPE_VALUES = {
    "randomized_experiment",
    "natural_experiment",
    "quasi_experiment",
    "observational_longitudinal",
    "observational_cross_sectional",
    "mechanistic_study",
    "structural_equation_model",
    "meta_analysis",
    "systematic_review",
    "modeling_simulation",
    "expert_judgment",
    "case_study",
    "theoretical",
    "indigenous_knowledge",
    "practitioner_experience",
}
EVIDENCE_TYPE_ALIASES = {
    "experiment": "quasi_experiment",
    "experimental": "quasi_experiment",
    "field_experiment": "quasi_experiment",
    "controlled_experiment": "quasi_experiment",
    "survey": "observational_cross_sectional",
    "survey_data": "observational_cross_sectional",
    "observational": "observational_cross_sectional",
    "observational_study": "observational_cross_sectional",
    "correlational_study": "observational_cross_sectional",
    "cross_sectional": "observational_cross_sectional",
    "longitudinal": "observational_longitudinal",
    "monitoring": "observational_longitudinal",
    "time_series": "observational_longitudinal",
    "mechanistic": "mechanistic_study",
    "mechanism": "mechanistic_study",
    "sem": "structural_equation_model",
    "modeling": "modeling_simulation",
    "simulation": "modeling_simulation",
    "model": "modeling_simulation",
    "review": "systematic_review",
}
EVIDENCE_OBJECT_VALUES = {"correlation", "mechanism", "both"}
EVIDENCE_OBJECT_ALIASES = {
    "correlational": "correlation",
    "association": "correlation",
    "statistical": "correlation",
    "survey": "correlation",
    "survey_data": "correlation",
    "observational_data": "correlation",
    "field_observations": "correlation",
    "experimental_data": "correlation",
    "difference_making": "correlation",
    "causal_mechanism": "mechanism",
    "mechanistic": "mechanism",
    "correlation_and_mechanism": "both",
    "mechanism_and_correlation": "both",
}
STRUCTURE_FIELDS = {
    "direction": {"status", "evidence_for_direction"},
    "mediation": {"status", "mediator_node_ids", "pathway_description"},
    "moderation": {"status", "moderator_node_ids", "interaction_type"},
    "strength": {
        "status",
        "quantitative_value",
        "quantitative_numeric",
        "qualitative_descriptor",
        "dose_response",
    },
    "context_dependence": {
        "status",
        "scope_conditions",
        "geographic_scope",
        "temporal_scope",
        "ecosystem_scope",
    },
    "temporal_extent": {
        "duration_months",
        "duration_text",
        "lag_months",
        "observation_grain",
        "observation_seasons",
    },
}


def stable_id(prefix: str, *parts: object) -> str:
    material = "|".join(str(part) for part in parts)
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}:{digest}"


def normalize_graph(graph: dict, source: dict | None = None) -> dict:
    """Convert extraction drafts and legacy output into CAMO v0.7.1 shape."""
    source = source or {}
    warnings: list[str] = []
    nodes = []
    id_map: dict[str, str] = {}
    normalized: dict
    for index, raw in enumerate(graph.get("nodes", [])):
        if not isinstance(raw, dict):
            warnings.append(f"nodes[{index}]: dropped non-object node")
            continue
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
            "entity_type": _canonical_enum(
                node.get("entity_type"),
                ENTITY_VALUES,
                ENTITY_ALIASES,
                "environmental_variable",
                f"nodes[{index}].entity_type",
                warnings,
            ),
            "entity_term": node.get("entity_term")
            or node.get("entity")
            or node.get("entity_mention")
            or "causal_mosaic:unresolved",
            "state_or_change_qualifier": _canonical_enum(
                node.get("state_or_change_qualifier") or node.get("state_qualifier"),
                STATE_VALUES,
                STATE_ALIASES,
                "unspecified",
                f"nodes[{index}].state_or_change_qualifier",
                warnings,
            ),
        }
        measured = node.get("measured_attribute") or node.get("attribute")
        if measured:
            normalized["measured_attribute"] = measured
        spans = _normalize_spans(
            node.get("source_spans"), f"nodes[{index}].source_spans", warnings
        )
        if spans:
            normalized["source_spans"] = spans
        nodes.append(normalized)

    edges = []
    for index, raw in enumerate(graph.get("edges", [])):
        if not isinstance(raw, dict):
            warnings.append(f"edges[{index}]: dropped non-object edge")
            continue
        edge = dict(raw)
        subject = str(edge.get("subject") or edge.get("subject_node_id") or "")
        object_ = str(edge.get("object") or edge.get("object_node_id") or "")
        evidence = edge.get("evidential_basis") or edge.get("evidence") or {}
        if not isinstance(evidence, dict):
            warnings.append(
                f"edges[{index}].evidential_basis: invalid object -> defaults"
            )
            evidence = {}
        accounts = (
            edge.get("philosophical_accounts")
            or edge.get("philosophical_account")
            or ["probabilistic"]
        )
        if isinstance(accounts, str):
            accounts = [accounts]
        normalized_accounts = _canonical_list(
            accounts,
            ACCOUNT_VALUES,
            ACCOUNT_ALIASES,
            "probabilistic",
            f"edges[{index}].philosophical_accounts",
            warnings,
        )
        raw_provenance = edge.get("prov")
        provenance: dict = raw_provenance if isinstance(raw_provenance, dict) else {}
        original_sentence = edge.get("original_sentence") or provenance.get(
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
            "predicate": _canonical_enum(
                edge.get("predicate"),
                PREDICATE_VALUES,
                PREDICATE_ALIASES,
                "associated_with",
                f"edges[{index}].predicate",
                warnings,
            ),
            "object": id_map.get(object_, object_),
            "claim_strength": _canonical_enum(
                edge.get("claim_strength"),
                CLAIM_VALUES,
                CLAIM_ALIASES,
                "associational",
                f"edges[{index}].claim_strength",
                warnings,
            ),
            "philosophical_accounts": normalized_accounts,
            "original_sentence": original_sentence,
            "source_spans": _normalize_spans(
                edge.get("source_spans") or [{"text": original_sentence}],
                f"edges[{index}].source_spans",
                warnings,
            ),
            "evidential_basis": _normalize_evidence(
                evidence, f"edges[{index}].evidential_basis", warnings
            ),
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
            "proportionality",
        ):
            feature_values = edge.get("features")
            if not isinstance(feature_values, dict):
                feature_values = {}
            value = edge.get(feature) or feature_values.get(feature)
            if value:
                normalized[feature] = _canonical_enum(
                    value,
                    FEATURE_VALUES,
                    FEATURE_ALIASES,
                    "not_addressed",
                    f"edges[{index}].{feature}",
                    warnings,
                )
        for structure in (
            "direction",
            "mediation",
            "moderation",
            "strength",
            "context_dependence",
            "temporal_extent",
        ):
            if edge.get(structure):
                normalized[structure] = _normalize_structure(
                    structure, edge[structure], f"edges[{index}].{structure}", warnings
                )
        _normalize_edge_enums(normalized, edge, index, warnings)
        for structure, field in (
            ("mediation", "mediator_node_ids"),
            ("moderation", "moderator_node_ids"),
        ):
            if structure in normalized and field in normalized[structure]:
                normalized[structure][field] = [
                    id_map.get(reference, reference)
                    for reference in _as_list(normalized[structure][field])
                ]
        edge_warnings = [
            warning for warning in warnings if warning.startswith(f"edges[{index}]")
        ]
        if edge_warnings:
            normalized["annotation_notes"] = "Normalization: " + "; ".join(
                edge_warnings
            )
        edges.append(normalized)

    graph_id = graph.get("graph_id") or stable_id(
        "causal_mosaic:graph", source.get("doi") or source.get("title") or "corpus"
    )
    normalized_graph = {
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
    if warnings:
        LOGGER.warning(
            "Canonicalized %d model value(s): %s",
            len(warnings),
            "; ".join(warnings[:10]) + ("; ..." if len(warnings) > 10 else ""),
        )
    return normalized_graph


def _normalize_spans(values: object, path: str, warnings: list[str]) -> list[dict]:
    spans = []
    for index, value in enumerate(_as_list(values) if values else []):
        if isinstance(value, str):
            warnings.append(f"{path}[{index}]: string -> TextSpan")
            value = {"text": value}
        if not isinstance(value, dict) or not value.get("text"):
            warnings.append(f"{path}[{index}]: dropped invalid TextSpan")
            continue
        span = {
            key: value[key]
            for key in ("text", "start_char", "end_char", "sentence_id", "paragraph_id")
            if value.get(key) not in (None, "")
        }
        for field in ("start_char", "end_char"):
            if field in span and not isinstance(span[field], int):
                try:
                    span[field] = int(span[field])
                    warnings.append(f"{path}[{index}].{field}: coerced to integer")
                except (TypeError, ValueError):
                    span.pop(field)
                    warnings.append(f"{path}[{index}].{field}: dropped invalid offset")
        spans.append(span)
    return spans


def _normalize_structure(
    name: str, value: object, path: str, warnings: list[str]
) -> dict | object:
    if not isinstance(value, dict):
        if name == "temporal_extent":
            warnings.append(f"{path}: scalar -> duration_text")
            return {"duration_text": str(value)}
        return value
    allowed = STRUCTURE_FIELDS[name]
    result = {key: item for key, item in value.items() if key in allowed}
    dropped = sorted(set(value) - allowed)
    if dropped:
        warnings.append(f"{path}: dropped unknown fields {dropped}")
    for field in (
        "mediator_node_ids",
        "moderator_node_ids",
        "scope_conditions",
        "observation_seasons",
    ):
        if field in result:
            result[field] = _as_list(result[field])
    for field in ("quantitative_numeric", "duration_months", "lag_months"):
        if field in result and not isinstance(result[field], (int, float)):
            try:
                result[field] = float(result[field])
                warnings.append(f"{path}.{field}: coerced to number")
            except (TypeError, ValueError):
                result.pop(field)
                warnings.append(f"{path}.{field}: dropped invalid number")
    if "dose_response" in result and not isinstance(result["dose_response"], bool):
        token = _token(result["dose_response"])
        if token in {"true", "yes", "present"}:
            result["dose_response"] = True
        elif token in {"false", "no", "absent"}:
            result["dose_response"] = False
        else:
            result.pop("dose_response")
            warnings.append(f"{path}.dose_response: dropped invalid boolean")
    return result


def _token(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return re.sub(r"[^a-z0-9]+", "_", str(value).casefold()).strip("_")


def _canonical_enum(
    value: object,
    allowed: set[str],
    aliases: dict[str, str],
    default: str,
    path: str,
    warnings: list[str],
) -> str:
    if value in (None, ""):
        return default
    token = _token(value)
    if token in allowed:
        return token
    if token in aliases:
        replacement = aliases[token]
        warnings.append(f"{path}: {value!r} -> {replacement!r}")
        return replacement
    warnings.append(f"{path}: unknown {value!r} -> {default!r}")
    return default


def _canonical_list(
    values: object,
    allowed: set[str],
    aliases: dict[str, str],
    default: str,
    path: str,
    warnings: list[str],
) -> list[str]:
    result = []
    for value in _as_list(values) if values not in (None, "") else []:
        canonical = _canonical_enum(value, allowed, aliases, default, path, warnings)
        if canonical not in result:
            result.append(canonical)
    return result or [default]


def _normalize_evidence(evidence: dict, path: str, warnings: list[str]) -> dict:
    raw_types = _as_list(
        evidence.get("evidence_types")
        or evidence.get("evidence_type")
        or evidence.get("type")
        or []
    )
    raw_objects = _as_list(
        evidence.get("evidence_objects")
        or evidence.get("evidence_object")
        or evidence.get("object")
        or []
    )
    evidence_types: list[str] = []
    evidence_objects: list[str] = []
    for bucket, values in (("type", raw_types), ("object", raw_objects)):
        for value in values:
            token = _token(value)
            target = None
            replacement = None
            if token in EVIDENCE_TYPE_VALUES:
                target, replacement = "type", token
            elif token in EVIDENCE_OBJECT_VALUES:
                target, replacement = "object", token
            elif bucket == "type" and token in EVIDENCE_TYPE_ALIASES:
                target, replacement = "type", EVIDENCE_TYPE_ALIASES[token]
            elif bucket == "object" and token in EVIDENCE_OBJECT_ALIASES:
                target, replacement = "object", EVIDENCE_OBJECT_ALIASES[token]
            elif token in EVIDENCE_TYPE_ALIASES:
                target, replacement = "type", EVIDENCE_TYPE_ALIASES[token]
            elif token in EVIDENCE_OBJECT_ALIASES:
                target, replacement = "object", EVIDENCE_OBJECT_ALIASES[token]
            if replacement is None:
                warnings.append(f"{path}.{bucket}s: dropped unknown {value!r}")
                continue
            if token != replacement or target != bucket:
                warnings.append(
                    f"{path}.{bucket}s: {value!r} -> {target} {replacement!r}"
                )
            destination = evidence_types if target == "type" else evidence_objects
            if replacement not in destination:
                destination.append(replacement)
    return {
        "evidence_types": evidence_types or ["observational_cross_sectional"],
        "evidence_objects": evidence_objects or ["correlation"],
    }


def _normalize_edge_enums(
    normalized: dict, edge: dict, index: int, warnings: list[str]
) -> None:
    features = edge.get("features", {})
    if not isinstance(features, dict):
        features = {}
    scalar_specs = {
        "token_or_type": (TOKEN_VALUES, TOKEN_ALIASES, "not_addressed"),
        "determinism": (DETERMINISM_VALUES, DETERMINISM_ALIASES, "not_addressed"),
        "proximate_distal": (PROXIMATE_VALUES, PROXIMATE_ALIASES, "not_addressed"),
        "contributing_sole": (
            CONTRIBUTING_VALUES,
            CONTRIBUTING_ALIASES,
            "not_addressed",
        ),
        "reversibility": (
            REVERSIBILITY_VALUES,
            REVERSIBILITY_ALIASES,
            "not_addressed",
        ),
    }
    for field, (allowed, aliases, default) in scalar_specs.items():
        value = edge.get(field) or features.get(field)
        if value not in (None, ""):
            normalized[field] = _canonical_enum(
                value,
                allowed,
                aliases,
                default,
                f"edges[{index}].{field}",
                warnings,
            )

    structure_specs = {
        "direction": (DIRECTION_STATUS_VALUES, DIRECTION_STATUS_ALIASES),
        "mediation": (FEATURE_VALUES, FEATURE_ALIASES),
        "moderation": (FEATURE_VALUES, FEATURE_ALIASES),
        "strength": (FEATURE_VALUES, FEATURE_ALIASES),
        "context_dependence": (FEATURE_VALUES, FEATURE_ALIASES),
    }
    for field, (allowed, aliases) in structure_specs.items():
        structure = normalized.get(field)
        if not structure:
            continue
        if not isinstance(structure, dict):
            structure = {"status": structure}
            normalized[field] = structure
        default = "not_addressed"
        structure["status"] = _canonical_enum(
            structure.get("status"),
            allowed,
            aliases,
            default,
            f"edges[{index}].{field}.status",
            warnings,
        )
    direction = normalized.get("direction", {})
    if direction.get("evidence_for_direction"):
        direction["evidence_for_direction"] = _canonical_enum(
            direction["evidence_for_direction"],
            DIRECTION_EVIDENCE_VALUES,
            DIRECTION_EVIDENCE_ALIASES,
            "theoretical",
            f"edges[{index}].direction.evidence_for_direction",
            warnings,
        )
    moderation = normalized.get("moderation", {})
    if moderation.get("interaction_type"):
        moderation["interaction_type"] = _canonical_enum(
            moderation["interaction_type"],
            INTERACTION_VALUES,
            INTERACTION_ALIASES,
            "not_specified",
            f"edges[{index}].moderation.interaction_type",
            warnings,
        )
    strength = normalized.get("strength", {})
    if strength.get("qualitative_descriptor"):
        strength["qualitative_descriptor"] = _canonical_enum(
            strength["qualitative_descriptor"],
            STRENGTH_VALUES,
            STRENGTH_ALIASES,
            "not_specified",
            f"edges[{index}].strength.qualitative_descriptor",
            warnings,
        )


class GraphValidationError(ValueError):
    """A compact report containing all remaining graph validation failures."""


def validate_graph(graph: dict) -> None:
    """Raise one compact exception containing all CAMO validation failures."""
    errors = sorted(_validator().iter_errors(graph), key=lambda error: list(error.path))
    messages = [_format_validation_error(error) for error in errors]
    node_ids = {node["id"] for node in graph.get("nodes", [])}
    for edge in graph.get("edges", []):
        if edge.get("subject") not in node_ids or edge.get("object") not in node_ids:
            messages.append(
                f"edges.{edge.get('id')}: dangling subject/object reference"
            )
        nested_references = [
            *edge.get("mediation", {}).get("mediator_node_ids", []),
            *edge.get("moderation", {}).get("moderator_node_ids", []),
        ]
        if any(reference not in node_ids for reference in nested_references):
            messages.append(
                f"edges.{edge.get('id')}: dangling mediator/moderator reference"
            )
    if messages:
        shown = messages[:25]
        suffix = f"\n... and {len(messages) - 25} more" if len(messages) > 25 else ""
        raise GraphValidationError(
            f"CAMO graph has {len(messages)} validation error(s):\n"
            + "\n".join(f"- {message}" for message in shown)
            + suffix
        )


def _format_validation_error(error: jsonschema.ValidationError) -> str:
    path = ".".join(str(part) for part in error.absolute_path) or "graph"
    details = []
    for context in error.context[:3]:
        context_path = ".".join(str(part) for part in context.relative_path)
        details.append(
            f"{context_path}: {context.message}" if context_path else context.message
        )
    return f"{path}: {error.message}" + (f" ({'; '.join(details)})" if details else "")


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
