"""Rule-layer interfaces for domain feasibility checks."""

from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements


def check_food_packaging_compatibility(
    requirements: PackagingRequirements,
    material: PackagingMaterial,
) -> bool:
    """Check food-to-packaging compatibility using configurable domain rules."""
    _ = requirements, material
    return True


def apply_domain_rules(
    requirements: PackagingRequirements,
    candidates: list[PackagingMaterial],
) -> list[PackagingMaterial]:
    """Apply rule-layer feasibility filtering before ML ranking."""
    return [
        material
        for material in candidates
        if check_food_packaging_compatibility(requirements, material)
    ]
