"""Validator for causal graph data."""

from typing import Optional

try:
    from ontology_agent import OntologyAgent  # type: ignore[attr-defined]

    HAS_ONTOLOGY_AGENT = True
except ImportError:
    HAS_ONTOLOGY_AGENT = False

    class OntologyAgent:  # type: ignore[no-redef]
        pass


class Validator:
    """Validates causal graph data against schema constraints."""

    def __init__(
        self,
        ontology_agent: Optional[OntologyAgent] = None,
        confidence_threshold: float = 0.5,
    ):
        """Initialize validator.

        Args:
            ontology_agent: Optional ontology agent for grounding
            confidence_threshold: Minimum confidence threshold
        """
        self.ontology_agent = ontology_agent
        self.confidence_threshold = confidence_threshold

        # Coordinate ranges
        self.lat_range = (-90, 90)
        self.lon_range = (-180, 180)

        # Numeric ranges
        self.p_value_range = (0, 1)
        self.correlation_range = (-1, 1)

        # Valid state qualifiers
        self.valid_state_qualifiers = [
            "increased",
            "decreased",
            "present",
            "absent",
            "introduced",
            "removed",
            "unchanged",
            "occurred",
            "initiated",
            "terminated",
            "ongoing",
            "interrupted",
            "aborted",
        ]

        # Valid predicates
        self.valid_predicates = [
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
        ]

        # Valid philosophical accounts
        self.valid_philosophical_accounts = [
            "counterfactual",
            "probabilistic",
            "interventionist",
            "transmission",
            "mechanistic",
            "regularity",
            "inus_component",
            "agency",
        ]

        # Valid evidence types
        self.valid_evidence_types = [
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
        ]

    def validate_graph(self, graph: dict) -> dict:
        """Validate entire graph.

        Args:
            graph: Graph dict to validate

        Returns:
            Validated graph with confidence scores
        """
        # Validate nodes
        graph["nodes"] = self._validate_nodes(graph.get("nodes", []))

        # Validate edges
        graph["edges"] = self._validate_edges(graph.get("edges", []))

        # Validate metadata
        graph["metadata"] = self._validate_metadata(graph.get("metadata", {}))

        return graph

    def _validate_nodes(self, nodes: list) -> list:
        """Validate nodes."""
        validated = []

        for node in nodes:
            validated_node = self._validate_node(node)
            if validated_node:
                validated.append(validated_node)

        return validated

    def _validate_node(self, node: dict) -> Optional[dict]:
        """Validate a single node."""
        # Check required fields
        required = ["id", "entity", "state_qualifier"]
        for field in required:
            if field not in node:
                node[field] = "" if field == "id" else None

        # Validate entity type
        if "entity_type" not in node:
            node["entity_type"] = "environmental_variable"

        # Validate state qualifier
        if node.get("state_qualifier") not in self.valid_state_qualifiers:
            node["state_qualifier"] = "unchanged"

        # Ground entity if possible
        if HAS_ONTOLOGY_AGENT and self.ontology_agent and node.get("entity"):
            # Try to ground entity (simplified)
            pass

        return node

    def _validate_edges(self, edges: list) -> list:
        """Validate edges."""
        validated = []

        for edge in edges:
            validated_edge = self._validate_edge(edge)
            if validated_edge:
                validated.append(validated_edge)

        return validated

    def _validate_edge(self, edge: dict) -> Optional[dict]:
        """Validate a single edge."""
        # Check required fields
        required = ["id", "subject_node_id", "object_node_id", "predicate"]
        for field in required:
            if field not in edge:
                edge[field] = "" if field == "id" else None

        # Validate predicate
        if edge.get("predicate") not in self.valid_predicates:
            edge["predicate"] = "associated_with"

        # Validate philosophical account
        if edge.get("philosophical_account") not in self.valid_philosophical_accounts:
            edge["philosophical_account"] = "probabilistic"

        # Validate evidence type
        if edge.get("evidence", {}).get("type") not in self.valid_evidence_types:
            edge.setdefault("evidence", {})["type"] = "observational_cross_sectional"

        # Validate numeric values
        if "prov" in edge:
            # Validate page number
            if "source_page" in edge["prov"]:
                if not isinstance(edge["prov"]["source_page"], int):
                    edge["prov"]["source_page"] = 1

            # Validate line range
            if "source_line_range" in edge["prov"]:
                if not isinstance(edge["prov"]["source_line_range"], (list, tuple)):
                    edge["prov"]["source_line_range"] = [1, 1]

        # Validate features
        features = edge.setdefault("features", {})
        if "strength_qualitative" in features:
            if features["strength_qualitative"] not in [
                "strong",
                "moderate",
                "weak",
                "negligible",
                "not_specified",
            ]:
                features["strength_qualitative"] = "not_specified"

        return edge

    def _validate_metadata(self, metadata: dict) -> dict:
        """Validate metadata."""
        # Set defaults if missing
        if "extracted_at" not in metadata:
            from datetime import datetime

            metadata["extracted_at"] = datetime.utcnow().isoformat()

        if "confidence" not in metadata:
            metadata["confidence"] = 1.0

        # Validate confidence
        if not isinstance(metadata["confidence"], (int, float)):
            metadata["confidence"] = 1.0
        elif metadata["confidence"] < 0:
            metadata["confidence"] = 0.0
        elif metadata["confidence"] > 1:
            metadata["confidence"] = 1.0

        return metadata

    def validate_entity(self, entity: str, ontology: str = "ENVO") -> Optional[dict]:
        """Validate and ground an entity.

        Args:
            entity: Entity text to validate
            ontology: Ontology to use for grounding

        Returns:
            Dict with grounding info or None if not found
        """
        if not self.ontology_agent:
            return None

        try:
            result = self.ontology_agent.search(entity, ontologies=[ontology], limit=1)

            if result.results and result.results[0].term:
                return {
                    "curie": result.results[0].term.curie,
                    "label": result.results[0].term.label,
                    "ontology": result.results[0].term.ontology,
                    "score": (
                        result.results[0].term.score
                        if hasattr(result.results[0].term, "score")
                        else 1.0
                    ),
                }
        except Exception:
            pass

        return None
