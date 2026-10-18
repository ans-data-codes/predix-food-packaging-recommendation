"""Storage and transport condition schemas."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class StorageConditions:
    """Storage and transport constraints for packaging decisions."""

    storage_type: str
    temperature: Optional[float] = None
    relative_humidity: Optional[float] = None
    transport_duration: Optional[float] = None
    handling_conditions: Optional[str] = None
