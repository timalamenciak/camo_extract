"""Consolidator for merging multiple causal graphs."""

from typing import Optional


class Consolidator:
    """Consolidates multiple causal graphs into a single graph."""

    def __init__(
        self,
        merge_duplicated_nodes: bool = True,
        deduplicate_edges: bool = True,
    ):
        """Initialize consolidator.

        Args:
            merge_duplicated_nodes: Whether to merge duplicate nodes
            deduplicate_edges: Whether to deduplicate edges
        """
        self.merge_duplicated_nodes = merge_duplicated_nodes
        self.deduplicate_edges = deduplicate_edges

    def consolidate(self, graphs: list[dict]) -> dict:
        """Consolidate multiple graphs.

        Args:
            graphs: List of graph dicts

        Returns:
            Consolidated graph dict
        """
        if not graphs:
            return {"nodes": [], "edges": [], "metadata": {}}

        # Collect all nodes and edges
        all_nodes: dict[str, dict] = {}
        all_edges: list[dict] = []

        node_id_counter = 0

        for graph in graphs:
            # Process nodes
            if self.merge_duplicated_nodes:
                for node in graph.get("nodes", []):
                    node_key = self._node_key(node)
                    if node_key not in all_nodes:
                        node_id = f"node_{node_id_counter}"
                        node_id_counter += 1
                        node["id"] = node_id
                        all_nodes[node_key] = node
                    else:
                        # Merge metadata
                        existing = all_nodes[node_key]
                        self._merge_metadata(existing, node)
            else:
                for node in graph.get("nodes", []):
                    if "id" not in node or not node["id"]:
                        node["id"] = f"node_{node_id_counter}"
                        node_id_counter += 1
                    all_nodes[node["id"]] = node

            # Process edges
            for edge in graph.get("edges", []):
                # Update node references if needed
                edge["subject_node_id"] = self._get_node_id(
                    edge.get("subject_node_id"), all_nodes
                )
                edge["object_node_id"] = self._get_node_id(
                    edge.get("object_node_id"), all_nodes
                )

                if "id" not in edge or not edge["id"]:
                    edge["id"] = f"edge_{len(all_edges)}"

                all_edges.append(edge)

        # Deduplicate edges if requested
        if self.deduplicate_edges:
            all_edges = self._deduplicate_edges(all_edges)

        # Build consolidated graph
        consolidated = {
            "nodes": list(all_nodes.values()),
            "edges": all_edges,
            "metadata": {
                "source_count": len(graphs),
                "total_nodes": len(all_nodes),
                "total_edges": len(all_edges),
            },
        }

        return consolidated

    def _node_key(self, node: dict) -> str:
        """Generate key for node deduplication."""
        # Use entity + attribute + state_qualifier as key
        parts = [
            node.get("entity", ""),
            node.get("attribute", ""),
            node.get("state_qualifier", ""),
        ]
        return "::".join(parts)

    def _merge_metadata(self, existing: dict, new: dict) -> None:
        """Merge metadata from new node into existing node."""
        for key, value in new.items():
            if key == "id":
                continue
            if key not in existing or not existing[key]:
                existing[key] = value
            elif key == "prov" and "prov" in existing:
                existing["prov"].append(value)

    def _get_node_id(self, node_ref: Optional[str], nodes: dict) -> str:
        """Get node ID from reference."""
        if not node_ref:
            return ""

        # If reference is a key in nodes dict
        if node_ref in nodes:
            return node_ref

        # Try to find by matching entity
        for node_key, node in nodes.items():
            if node.get("entity") == node_ref:
                return node["id"]

        return node_ref

    def _deduplicate_edges(self, edges: list) -> list:
        """Remove duplicate edges."""
        seen = set()
        deduplicated = []

        for edge in edges:
            key = self._edge_key(edge)
            if key not in seen:
                seen.add(key)
                deduplicated.append(edge)

        return deduplicated

    def _edge_key(self, edge: dict) -> str:
        """Generate key for edge deduplication."""
        # Use subject, object, predicate as key
        parts = [
            edge.get("subject_node_id", ""),
            edge.get("object_node_id", ""),
            edge.get("predicate", ""),
        ]
        return "::".join(parts)
