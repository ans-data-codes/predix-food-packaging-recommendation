"""Compatibility interfaces across MAP and storage constraints."""

from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements
from src.schemas.storage import StorageConditions


def check_map_compatibility(material: PackagingMaterial, requirements: PackagingRequirements) -> bool:
    """Check MAP compatibility using future commodity- and condition-specific guidelines."""
    if requirements.MAP_required is None:
        return True
    return material.MAP_compatibility in (None, requirements.MAP_required)


def check_storage_compatibility(material: PackagingMaterial, storage: StorageConditions) -> bool:
    """Check storage compatibility using future rule and evidence sources."""
    _ = material, storage
    return True
