"""Validation interfaces for incoming structured inputs."""

from src.schemas.food import FoodInput
from src.schemas.storage import StorageConditions


def validate_food_input(food: FoodInput) -> FoodInput:
    """Validate food input structure without scientific thresholds."""
    if not food.commodity_type:
        raise ValueError("commodity_type is required")
    return food


def validate_storage_conditions(storage: StorageConditions) -> StorageConditions:
    """Validate storage condition structure without scientific thresholds."""
    if not storage.storage_type:
        raise ValueError("storage_type is required")
    return storage
