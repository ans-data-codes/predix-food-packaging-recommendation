"""Packaging material schemas."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class TransmissionMeasurement:
    """Measured barrier value with explicit test context."""

    value: Optional[float] = None
    unit: Optional[str] = None
    thickness: Optional[float] = None
    thickness_unit: Optional[str] = None
    test_conditions: Optional[str] = None
    source_reference: Optional[str] = None
    uncertainty: Optional[str] = None
    notes: Optional[str] = None


@dataclass
class PackagingMaterial:
    """Candidate packaging material profile."""

    material_id: str
    material_name: str
    material_family: Optional[str] = None
    OTR: list[TransmissionMeasurement] = field(default_factory=list)
    WVTR: list[TransmissionMeasurement] = field(default_factory=list)
    thickness: Optional[float] = None
    mechanical_strength: Optional[str] = None
    sealability: Optional[str] = None
    cost: Optional[float] = None
    recyclability: Optional[str] = None
    biodegradability: Optional[str] = None
    MAP_compatibility: Optional[bool] = None
    intended_use: Optional[str] = None
    source_reference: Optional[str] = None
    test_conditions: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)
