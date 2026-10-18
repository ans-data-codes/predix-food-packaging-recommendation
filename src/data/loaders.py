"""Data loading interfaces for input ingestion."""

from typing import Any


def load_input_data(payload: dict[str, Any]) -> dict[str, Any]:
    """Load raw user payload into an internal dictionary representation."""
    return dict(payload)
