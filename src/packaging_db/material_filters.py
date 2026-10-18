"""Filtering interfaces for packaging candidate selection."""

from src.knowledge.compatibility import check_map_compatibility, check_storage_compatibility
from src.knowledge.rules import check_food_packaging_compatibility
from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements
from src.schemas.storage import StorageConditions


def filter_materials_by_compatibility(
    materials: list[PackagingMaterial],
    requirements: PackagingRequirements,
) -> list[PackagingMaterial]:
    """Filter materials by high-level compatibility constraints."""
    return [m for m in materials if check_food_packaging_compatibility(requirements, m)]


def filter_by_barrier_requirements(
    materials: list[PackagingMaterial],
    requirements: PackagingRequirements,
) -> list[PackagingMaterial]:
    """Filter materials by barrier requirements using future barrier-rule logic."""
    _ = requirements
    return list(materials)


def filter_by_storage_conditions(
    materials: list[PackagingMaterial],
    storage: StorageConditions,
) -> list[PackagingMaterial]:
    """Filter materials by storage and transport compatibility constraints."""
    return [m for m in materials if check_storage_compatibility(m, storage)]


def get_material_candidates(
    materials: list[PackagingMaterial],
    requirements: PackagingRequirements,
    storage: StorageConditions,
) -> list[PackagingMaterial]:
    """Compose compatibility and requirement filters into candidate retrieval."""
    candidates = filter_materials_by_compatibility(materials, requirements)
    candidates = [m for m in candidates if check_map_compatibility(m, requirements)]
    candidates = filter_by_barrier_requirements(candidates, requirements)
    return filter_by_storage_conditions(candidates, storage)
