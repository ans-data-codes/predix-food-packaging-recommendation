"""Recommendation-related schemas."""

from dataclasses import dataclass, field
from typing import Any, Optional

from .packaging import PackagingMaterial


@dataclass
class PackagingRequirements:
    """Derived packaging requirements used for candidate filtering and ranking."""

    required_oxygen_barrier: Optional[str] = None
    required_moisture_barrier: Optional[str] = None
    preferred_OTR_range: Optional[tuple[float, float]] = None
    preferred_WVTR_range: Optional[tuple[float, float]] = None
    thickness_range: Optional[tuple[float, float]] = None
    mechanical_requirement: Optional[str] = None
    sealability_requirement: Optional[str] = None
    MAP_required: Optional[bool] = None
    breathable_packaging_required: Optional[bool] = None
    special_constraints: list[str] = field(default_factory=list)


@dataclass
class ShelfLifeAssessment:
    """Placeholder structure for shelf-life estimation outputs."""

    estimate: Optional[float] = None
    confidence: Optional[float] = None
    assumptions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class RecommendationResult:
    """Structured output for the final recommendation stage."""

    material: Optional[PackagingMaterial] = None
    packaging_structure: Optional[str] = None
    suitability_score: Optional[float] = None
    confidence_score: Optional[float] = None
    recommended_specs: dict[str, Any] = field(default_factory=dict)
    shelf_life_estimate: Optional[ShelfLifeAssessment] = None
    cost_score: Optional[float] = None
    sustainability_score: Optional[float] = None
    reasons: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    alternatives: list[PackagingMaterial] = field(default_factory=list)
