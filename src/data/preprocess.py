"""Normalization and preparation interfaces for user inputs."""

from typing import Any

from src.schemas.food import FoodInput
from src.schemas.storage import StorageConditions


def normalize_units(raw_data: dict[str, Any]) -> dict[str, Any]:
    """Normalize units where explicit conversions are later configured."""
    return dict(raw_data)


def prepare_input(food: FoodInput, storage: StorageConditions) -> tuple[FoodInput, StorageConditions]:
    """Prepare validated and normalized input objects for downstream pipelines."""
    return food, storage
