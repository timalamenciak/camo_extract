"""Backwards-compatible facade for CAMO LinkML validation."""

from __future__ import annotations

from .schema_validation import validate_graph


class Validator:
    """Validate a completed CAMO graph or raise a descriptive exception."""

    def __init__(self, *_, **__):
        pass

    def validate_graph(self, graph: dict) -> dict:
        validate_graph(graph)
        return graph
