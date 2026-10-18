"""Repository interfaces for packaging-material data access."""

from src.schemas.packaging import PackagingMaterial


def load_packaging_database() -> list[PackagingMaterial]:
    """Load packaging-material records from configured data sources."""
    return []


def get_material_by_id(material_id: str, materials: list[PackagingMaterial]) -> PackagingMaterial | None:
    """Get a material by id from an in-memory material list."""
    for material in materials:
        if material.material_id == material_id:
            return material
    return None
