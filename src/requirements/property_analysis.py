"""Property analysis interfaces for identifying packaging drivers."""

from src.schemas.food import FoodInput
from src.schemas.storage import StorageConditions


def analyze_food_properties(food: FoodInput) -> dict[str, object]:
    """Extract food-property signals relevant to packaging decisions."""
    return {
        "commodity_type": food.commodity_type,
        "moisture_content": food.moisture_content,
        "fat_content": food.fat_content,
        "water_activity": food.water_activity,
        "respiration_rate": food.respiration_rate,
    }


def analyze_storage_conditions(storage: StorageConditions) -> dict[str, object]:
    """Extract storage and transport signals relevant to packaging decisions."""
    return {
        "storage_type": storage.storage_type,
        "temperature": storage.temperature,
        "relative_humidity": storage.relative_humidity,
        "transport_duration": storage.transport_duration,
        "handling_conditions": storage.handling_conditions,
    }


def identify_packaging_drivers(
    food_analysis: dict[str, object],
    storage_analysis: dict[str, object],
) -> dict[str, object]:
    """Combine analyses into future configurable packaging-driver signals."""
    return {
        "food_drivers": food_analysis,
        "storage_drivers": storage_analysis,
        "rule_source": "knowledge_base_configuration",
    }
