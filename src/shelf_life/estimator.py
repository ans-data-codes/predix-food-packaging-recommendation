"""Shelf-life estimation placeholders."""

from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements, ShelfLifeAssessment


def estimate_shelf_life(
    material: PackagingMaterial,
    requirements: PackagingRequirements,
) -> ShelfLifeAssessment:
    """Placeholder for literature-backed shelf-life estimation models."""
    _ = material, requirements
    return ShelfLifeAssessment(
        estimate=None,
        confidence=None,
        assumptions=["Shelf-life model is not implemented yet."],
        warnings=["No scientific shelf-life equation has been applied in this prototype."],
    )


def estimate_degradation_risk(
    material: PackagingMaterial,
    requirements: PackagingRequirements,
) -> dict[str, object]:
    """Placeholder for degradation risk modeling."""
    _ = material, requirements
    return {"risk_level": None, "status": "pending_validated_model"}


def compare_shelf_life_options(
    assessments: list[ShelfLifeAssessment],
) -> list[ShelfLifeAssessment]:
    """Placeholder sorter for shelf-life options when models are available."""
    return assessments
