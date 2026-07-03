"""Reference-safe consolidation of CAMO graphs."""

from __future__ import annotations

from copy import deepcopy

from .schema_validation import stable_id


class Consolidator:
    def __init__(
        self, merge_duplicated_nodes: bool = True, deduplicate_edges: bool = True
    ):
        self.merge_duplicated_nodes = merge_duplicated_nodes
        self.deduplicate_edges = deduplicate_edges

    def consolidate(self, graphs: list[dict]) -> dict:
        if not graphs:
            return {
                "graph_id": stable_id("causal_mosaic:graph", "empty"),
                "schema_version": "0.7.1",
                "provenance": {
                    "ontology_framework": "ELMO + ENVO + Wikidata + CAMO",
                    "causal_mosaic_version": "0.7.1",
                },
                "nodes": [],
                "edges": [],
            }
        nodes_by_key: dict[tuple, dict] = {}
        edges = []
        for graph in graphs:
            id_map = {}
            for original in graph.get("nodes", []):
                node = deepcopy(original)
                key = (
                    self._node_key(node)
                    if self.merge_duplicated_nodes
                    else (node.get("id"),)
                )
                if key not in nodes_by_key:
                    node["id"] = stable_id("causal_mosaic:node", *key)
                    nodes_by_key[key] = node
                else:
                    self._merge_node(nodes_by_key[key], node)
                id_map[original.get("id")] = nodes_by_key[key]["id"]
            for original_edge in graph.get("edges", []):
                edge = deepcopy(original_edge)
                edge["subject"] = id_map.get(edge.get("subject"), edge.get("subject"))
                edge["object"] = id_map.get(edge.get("object"), edge.get("object"))
                for structure, field in (
                    ("mediation", "mediator_node_ids"),
                    ("moderation", "moderator_node_ids"),
                ):
                    if structure in edge and field in edge[structure]:
                        edge[structure][field] = [
                            id_map.get(reference, reference)
                            for reference in edge[structure][field]
                        ]
                edge["id"] = stable_id(
                    "causal_mosaic:edge",
                    edge.get("subject"),
                    edge.get("predicate"),
                    edge.get("object"),
                    edge.get("original_sentence"),
                    edge.get("source_document", {}).get("doi"),
                )
                edges.append(edge)
        if self.deduplicate_edges:
            unique: dict[tuple, dict] = {}
            for edge in edges:
                unique.setdefault(self._edge_key(edge), edge)
            edges = list(unique.values())
        first = graphs[0]
        return {
            "graph_id": stable_id(
                "causal_mosaic:graph", *(graph.get("graph_id", "") for graph in graphs)
            ),
            "schema_version": "0.7.1",
            "provenance": deepcopy(first.get("provenance", {})),
            "nodes": list(nodes_by_key.values()),
            "edges": edges,
        }

    @staticmethod
    def _node_key(node: dict) -> tuple:
        return (
            node.get("entity_term", ""),
            node.get("measured_attribute", ""),
            node.get("state_or_change_qualifier", ""),
            node.get("entity_type", ""),
        )

    @staticmethod
    def _merge_node(existing: dict, incoming: dict) -> None:
        spans = existing.setdefault("source_spans", [])
        for span in incoming.get("source_spans", []):
            if span not in spans:
                spans.append(span)

    @staticmethod
    def _edge_key(edge: dict) -> tuple:
        return (
            edge.get("subject"),
            edge.get("predicate"),
            edge.get("object"),
            edge.get("original_sentence"),
            edge.get("source_document", {}).get("doi"),
        )
