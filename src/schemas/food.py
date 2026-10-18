"""Food-related input schemas."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FoodInput:
    """Structured food/commodity input used by recommendation pipelines."""

    commodity_type: str
    moisture_content: Optional[float] = None
    fat_content: Optional[float] = None
    pH: Optional[float] = None
    water_activity: Optional[float] = None
    respiration_rate: Optional[float] = None
    target_shelf_life: Optional[float] = None
    notes: Optional[str] = None
