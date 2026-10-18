"""Core domain schemas."""

from .food import FoodInput
from .packaging import PackagingMaterial, TransmissionMeasurement
from .recommendation import PackagingRequirements, RecommendationResult, ShelfLifeAssessment
from .storage import StorageConditions

__all__ = [
    "FoodInput",
    "StorageConditions",
    "TransmissionMeasurement",
    "PackagingMaterial",
    "PackagingRequirements",
    "ShelfLifeAssessment",
    "RecommendationResult",
]
