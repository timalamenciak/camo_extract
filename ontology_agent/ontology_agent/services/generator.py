"""Term suggestion generator.

When no appropriate term is found in ontology searches, this module
generates intelligent suggestions including:
- Suggested term label
- Recommended ontology (ENVO, BFO, PATO, etc.)
- BFO hierarchy position
- Proposed definition

The generator analyzes the query and maps it to appropriate ontological concepts.
"""

from __future__ import annotations

from typing import Optional

from ..models import TermSuggestion


class TermGenerator:
    """Generate ontology term suggestions when no match is found."""

    BFO_CLASSES = {
        "BFO:0000002": "continuant",
        "BFO:0000003": "occurrent",
        "BFO:0000004": "independent_continuant",
        "BFO:0000015": "process",
        "BFO:0000020": "quality",
        "BFO:0000038": "generically_dependent_continuant",
        "BFO:0000050": "spatiotemporal_region",
    }

    ONTOLOGY_RECOMMENDATIONS = {
        "environmental": "ENVO",
        "environment": "ENVO",
        " geographical": "ENVO",
        "location": "ENVO",
        "process": "GO",
        "biological": "GO",
        "molecular": "GO",
        "quality": "PATO",
        "phenotypic": "PATO",
        "material": "CHEBI",
        "chemical": "CHEBI",
        "entity": "BFO",
        "thing": "BFO",
        "object": "BFO",
        "state": "BFO",
        "property": "PATO",
        "attribute": "PATO",
        "growth": "PATO",
        "rate": "PATO",
        "development": "PATO",
        "population": "PATO",
    }

    def __init__(self, preferred_ontology: Optional[str] = None):
        self.preferred_ontology = preferred_ontology

    def generate_suggestions(
        self,
        query: str,
        ontologies_searched: list[str],
        limit: int = 3,
    ) -> list[TermSuggestion]:
        """Generate term suggestions for a query.

        Args:
            query: The original search query
            ontologies_searched: List of ontologies that were searched
            limit: Maximum number of suggestions

        Returns:
            List of TermSuggestion objects
        """
        if not query or not query.strip():
            return []

        query_normalized = query.strip().lower()
        suggestions = []

        entity_type = self._classify_entity(query_normalized)
        bfo_class = self._map_to_bfo(entity_type)
        recommended_ontology = self._select_ontology(entity_type, ontologies_searched)

        if recommended_ontology == "BFO":
            suggestion = self._generate_bfo_suggestion(query, bfo_class)
            if suggestion:
                suggestions.append(suggestion)
        else:
            suggestion = self._generate_generic_suggestion(
                query, recommended_ontology, bfo_class, entity_type
            )
            if suggestion:
                suggestions.append(suggestion)

        if len(suggestions) < limit:
            alt_ontology = self._get_alternative_ontology(recommended_ontology)
            if alt_ontology:
                alt_suggestion = self._generate_generic_suggestion(
                    query, alt_ontology, bfo_class, entity_type
                )
                if alt_suggestion:
                    alt_suggestion.score *= 0.8
                    suggestions.append(alt_suggestion)

        for i, suggestion in enumerate(suggestions):
            suggestion.score = suggestion.score * (1.0 - (i * 0.1))

        return suggestions[:limit]

    def _classify_entity(self, query: str) -> str:
        """Classify the type of entity based on query content."""
        query_lower = query.lower()

        environmental_keywords = [
            "environment",
            "habitat",
            "ecosystem",
            "biome",
            "physical",
            "abiotic",
            " geographical",
            " spatial",
            "location",
            "region",
            "zone",
            "grassland",
            "forest",
            "savanna",
            "tundra",
            "desert",
            "marine",
            "freshwater",
            "terrestrial",
            "landscape",
            "ecological",
            "habitats",
            "environments",
            "temperate",
            "tropical",
            "polar",
            "arid",
            "coastal",
            "wetland",
            "mountain",
            "valley",
            "plateau",
            "basin",
            "plain",
            "field",
            "meadow",
            "prairie",
            "rangeland",
            "woodland",
            "boreal",
            "bamboo",
            " mangrove",
            "kelp",
            "coral",
            "reef",
            "glacial",
            "permafrost",
            "volcanic",
            "canyon",
            "cave",
            "cavern",
            "island",
            "archipelago",
            "peninsula",
            "delta",
            "estuary",
            "fjord",
            "lagoon",
            "sand dune",
            "oasis",
            "steppe",
            "moor",
            "heath",
            "fen",
            "bog",
            "marsh",
            "swamp",
            "rainforest",
            "woodland",
            "thornscrub",
            "chaparral",
        ]
        process_keywords = [
            "process",
            "activity",
            "behavior",
            "action",
            "transformation",
            "development",
            "evolution",
            "division",
            "metabolism",
            "biosynthesis",
            "replication",
            "signaling",
            "signalling",
            "transport",
        ]
        quality_keywords = [
            "quality",
            "property",
            "attribute",
            "characteristic",
            "state",
            "condition",
            "amount",
            "degree",
            "intensity",
            "rate",
        ]
        material_keywords = [
            "material",
            "substance",
            "chemical",
            "compound",
            "element",
            "mixture",
            "molecule",
            "atom",
            "ion",
            "protein",
            "dna",
            "rna",
            "carbohydrate",
            "lipid",
            "protein",
            "enzyme",
            "substrate",
            "reagent",
            "solution",
            "buffer",
        ]

        environmental_score = sum(
            1 for kw in environmental_keywords if kw in query_lower
        )
        process_score = sum(1 for kw in process_keywords if kw in query_lower)
        quality_score = sum(1 for kw in quality_keywords if kw in query_lower)
        material_score = sum(1 for kw in material_keywords if kw in query_lower)

        scores = {
            "process": process_score,
            "quality": quality_score,
            "environmental": environmental_score,
            "material": material_score,
        }

        score_values = list(scores.values())
        max_score = max(score_values)
        if max_score > 0:
            for k, v in scores.items():
                if v == max_score:
                    return k
        return "general"

    def _map_to_bfo(self, entity_type: str) -> str:
        """Map entity type to BFO class."""
        mapping = {
            "environmental": "BFO:0000004",
            "process": "BFO:0000015",
            "quality": "BFO:0000020",
            "material": "BFO:0000004",
            "general": "BFO:0000004",
        }
        return mapping.get(entity_type, "BFO:0000004")

    def _select_ontology(self, entity_type: str, ontologies_searched: list[str]) -> str:
        """Select the most appropriate ontology for the entity type."""
        if self.preferred_ontology:
            return self.preferred_ontology

        ontology_mapping = {
            "environmental": "ENVO",
            "process": "GO",
            "quality": "PATO",
            "material": "CHEBI",
            "general": "PATO",
        }

        recommended = ontology_mapping.get(entity_type, "PATO")

        return recommended

    def _get_alternative_ontology(self, primary: str) -> Optional[str]:
        """Get an alternative ontology for fallback."""
        alternatives = {
            "ENVO": "GO",
            "GO": "ENVO",
            "PATO": "CHEBI",
            "CHEBI": "PATO",
            "BFO": None,
        }
        return alternatives.get(primary)

    def _generate_bfo_suggestion(
        self, query: str, bfo_class: str
    ) -> Optional[TermSuggestion]:
        """Generate a BFO hierarchy-based suggestion."""
        bfo_label = self.BFO_CLASSES.get(bfo_class, "entity")

        return TermSuggestion(
            term=query.title(),
            ontology="BFO",
            bfo_class=bfo_class,
            bfo_label=bfo_label,
            definition=f"A {bfo_label} that corresponds to the concept '{query}'.",
            justification=f"Query maps to BFO {bfo_label} class.",
            score=0.7,
        )

    def _generate_generic_suggestion(
        self,
        query: str,
        ontology: str,
        bfo_class: str,
        entity_type: str,
    ) -> TermSuggestion:
        """Generate a generic term suggestion."""
        bfo_label = self.BFO_CLASSES.get(bfo_class, "entity")

        return TermSuggestion(
            term=query.title(),
            ontology=ontology,
            bfo_class=bfo_class,
            bfo_label=bfo_label,
            definition=self._generate_definition(query, ontology, entity_type),
            justification=f"Entity type '{entity_type}' maps to {ontology} ontology.",
            score=0.85,
        )

    def _generate_definition(self, query: str, ontology: str, entity_type: str) -> str:
        """Generate a definition for the suggested term."""
        if ontology == "ENVO":
            return f"An environmental entity or process related to '{query}', representing a specific aspect of the environment."
        elif ontology == "GO":
            return f"A biological process, function, or component related to '{query}' in the Gene Ontology framework."
        elif ontology == "PATO":
            return f"A quality or phenotypic attribute of '{query}' as described in the Phenotypic Quality Ontology."
        elif ontology == "CHEBI":
            return f"A chemical entity or material related to '{query}' in the Chemical Entities of Biological Interest ontology."
        else:
            return f"A '{query}' entity in the {ontology} ontology."

    def estimate_bfo_hierarchy_path(self, bfo_class: str) -> list[tuple[str, str]]:
        """Estimate the path from root to the given BFO class.

        Args:
            bfo_class: The target BFO class CURIE

        Returns:
            List of (curie, label) tuples representing the hierarchy path
        """
        path = []

        if bfo_class == "BFO:0000002":
            path = [("BFO:0000001", "entity"), ("BFO:0000002", "continuant")]
        elif bfo_class == "BFO:0000003":
            path = [("BFO:0000001", "entity"), ("BFO:0000003", "occurrent")]
        elif bfo_class == "BFO:0000004":
            path = [
                ("BFO:0000001", "entity"),
                ("BFO:0000002", "continuant"),
                ("BFO:0000004", "independent_continuant"),
            ]
        elif bfo_class == "BFO:0000015":
            path = [
                ("BFO:0000001", "entity"),
                ("BFO:0000003", "occurrent"),
                ("BFO:0000015", "process"),
            ]
        elif bfo_class == "BFO:0000020":
            path = [
                ("BFO:0000001", "entity"),
                ("BFO:0000002", "continuant"),
                ("BFO:0000020", "quality"),
            ]

        return path


def generate_suggestions(
    query: str,
    ontologies_searched: list[str],
    preferred_ontology: Optional[str] = None,
    limit: int = 3,
    include_hierarchy_path: bool = False,
) -> tuple[list[TermSuggestion], Optional[str]]:
    """Convenience function to generate term suggestions.

    Args:
        query: The search query
        ontologies_searched: List of ontologies that were searched
        preferred_ontology: Optional preferred ontology
        limit: Maximum number of suggestions
        include_hierarchy_path: Whether to include full hierarchy path

    Returns:
        Tuple of (suggestions, best_bfo_class)
    """
    generator = TermGenerator(preferred_ontology=preferred_ontology)

    suggestions = generator.generate_suggestions(query, ontologies_searched, limit)

    best_bfo = None
    if suggestions:
        best_bfo = suggestions[0].bfo_class

    if include_hierarchy_path and best_bfo:
        for suggestion in suggestions:
            suggestion.bfo_class = best_bfo

    return suggestions, best_bfo
