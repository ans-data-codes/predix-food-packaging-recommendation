"""Interfaces for retrieving relevant guidelines and evidence metadata."""


def get_relevant_guidelines(context: dict[str, object]) -> list[dict[str, object]]:
    """Return structured guideline metadata for future evidence-backed rules."""
    return [{"context": context, "status": "to_be_populated_with_verified_sources"}]
