"""Command-line interface for the ontology agent.

Usage:
    ontology-agent search "temperate grassland" --ontology ENVO
    ontology-agent search "cell division" --include-suggestions
    ontology-agent term ENVO:00001001
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional

from .models import SearchStatus
from .services import OntologyAgent


def format_result(
    result: dict,
    verbose: bool = False,
    indent: int = 2,
) -> str:
    """Format a search result as a human-readable string."""
    output = []

    if result.get("status") == "found":
        output.append("Terms found")
    elif result.get("status") == "partial":
        output.append("No exact match found - suggestions generated:")
    else:
        output.append("No match found")

    if "results" in result:
        for i, r in enumerate(result["results"], 1):
            if r.get("term"):
                term = r["term"]
                label = term.get("label", "Unknown")
                if term.get("is_preferred", False):
                    label = f"[PREFERRED] {label}"
                output.append(f"\n{i}. {label}")
                output.append(f"   CURIE: {term.get('curie', 'N/A')}")
                output.append(f"   Ontology: {term.get('ontology', 'N/A')}")
                if term.get("synonyms") and len(term["synonyms"]) > 0:
                    synonyms_str = ", ".join(term["synonyms"][:5])
                    if len(term["synonyms"]) > 5:
                        synonyms_str += f" (+{len(term['synonyms']) - 5} more)"
                    output.append(f"   Synonyms: {synonyms_str}")
                if verbose and term.get("definition"):
                    output.append(f"   Definition: {term['definition'][:200]}")
                if term.get("hierarchy"):
                    h = term["hierarchy"]
                    if h and h.get("bfo_class"):
                        output.append(f"   BFO: {h['bfo_class']}")
            else:
                output.append(f"\n{i}. Suggested term:")
                for suggestion in r.get("suggestions", []):
                    output.append(f"   - {suggestion.get('term', 'N/A')}")
                    output.append(f"     Ontology: {suggestion.get('ontology', 'N/A')}")
                    if verbose:
                        output.append(f"     BFO: {suggestion.get('bfo_class', 'N/A')}")
                        output.append(
                            f"     Definition: {suggestion.get('definition', 'N/A')[:200]}"
                        )
                        output.append(
                            f"     Justification: {suggestion.get('justification', 'N/A')}"
                        )

    if "elapsed_ms" in result:
        output.append(f"\n_elapsed: {result['elapsed_ms']:.2f} ms")

    if verbose:
        output.append("\n_metadata:")
        output.append(f"   Status: {result.get('status', 'N/A')}")
        output.append(f"   Matches found: {result.get('matches_found', 0)}")
        output.append(
            f"   Suggestions generated: {result.get('suggestions_generated', 0)}"
        )

    return "\n".join(output)


def cmd_search(
    query: str,
    ontology: Optional[str] = None,
    ontologies: Optional[list[str]] = None,
    include_suggestions: bool = True,
    verbose: bool = False,
    json_output: bool = False,
    config_path: Optional[str] = None,
) -> int:
    """Execute a search query."""
    agent = OntologyAgent(config_path=config_path)

    result = agent.search(
        query=query,
        preferred_ontology=ontology,
        ontologies=ontologies or [],
        include_suggestions=include_suggestions,
        limit=10,
    )

    if json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2))
    else:
        print(format_result(result.model_dump(mode="json"), verbose=verbose))

    return 0 if result.status == SearchStatus.FOUND else 1


def cmd_term(
    curie: str,
    verbose: bool = False,
    json_output: bool = False,
    config_path: Optional[str] = None,
) -> int:
    """Look up a term by its CURIE."""
    agent = OntologyAgent(config_path=config_path)

    result = agent.find_term_by_curie(curie=curie)

    if result is None:
        print(f"Term not found: {curie}")
        return 1

    term_data = result.term.model_dump() if result.term else {}
    term_data["found"] = result.found

    if json_output:
        print(json.dumps(term_data, indent=2))
    else:
        if result.found and result.term:
            print("Term found")
            print(f"  Label: {result.term.label}")
            print(f"  CURIE: {result.term.curie}")
            print(f"  Ontology: {result.term.ontology}")
            if verbose and result.term.definition:
                print(f"  Definition: {result.term.definition}")
        else:
            print(f"Term not found: {curie}")
            return 1

    return 0


def main(args: Optional[list[str]] = None) -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="ontology-agent",
        description="Standalone ontology lookup agent with term suggestion capabilities",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Include additional details in output",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--config",
        help="Path to YAML configuration file",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search for ontology terms")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument(
        "-o",
        "--ontology",
        help="Preferred ontology (e.g., ENVO, BFO)",
    )
    search_parser.add_argument(
        "--ontologies",
        help="Comma-separated list of ontologies to search",
    )
    search_parser.add_argument(
        "--no-suggestions",
        action="store_true",
        help="Disable term suggestions",
    )

    term_parser = subparsers.add_parser("term", help="Look up a term by CURIE")
    term_parser.add_argument("curie", help="Full CURIE (e.g., ENVO:00001001)")

    parsed = parser.parse_args(args)

    if not parsed.command:
        parser.print_help()
        return 1

    if parsed.command == "search":
        ontologies_list = None
        if parsed.ontologies:
            ontologies_list = [o.strip() for o in parsed.ontologies.split(",")]

        return cmd_search(
            query=parsed.query,
            ontology=parsed.ontology,
            ontologies=ontologies_list,
            include_suggestions=not parsed.no_suggestions,
            verbose=parsed.verbose,
            json_output=parsed.json,
            config_path=parsed.config,
        )

    elif parsed.command == "term":
        return cmd_term(
            curie=parsed.curie,
            verbose=parsed.verbose,
            json_output=parsed.json,
            config_path=parsed.config,
        )

    return 1


if __name__ == "__main__":
    sys.exit(main())
