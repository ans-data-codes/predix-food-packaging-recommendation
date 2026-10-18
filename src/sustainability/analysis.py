"""Sustainability evaluation interfaces."""

from src.schemas.packaging import PackagingMaterial


def evaluate_recyclability(material: PackagingMaterial) -> float:
    """Placeholder recyclability evaluation."""
    _ = material
    return 0.0


def evaluate_biodegradability(material: PackagingMaterial) -> float:
    """Placeholder biodegradability evaluation."""
    _ = material
    return 0.0


def calculate_sustainability_score(material: PackagingMaterial) -> float:
    """Combine sustainability sub-scores with future configurable logic."""
    return (evaluate_recyclability(material) + evaluate_biodegradability(material)) / 2


def find_sustainable_alternatives(
    materials: list[PackagingMaterial],
    minimum_score: float = 0.0,
) -> list[PackagingMaterial]:
    """Return materials that satisfy minimum sustainability score threshold."""
    return [m for m in materials if calculate_sustainability_score(m) >= minimum_score]
