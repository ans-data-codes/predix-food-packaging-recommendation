"""Scoring interfaces for multi-criteria candidate evaluation."""

from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements
from src.ranking.weights import RankingWeights


def calculate_barrier_score(material: PackagingMaterial, requirements: PackagingRequirements) -> float:
    """Placeholder for barrier-fit scoring logic."""
    _ = material, requirements
    return 0.0


def calculate_shelf_life_score(material: PackagingMaterial, requirements: PackagingRequirements) -> float:
    """Placeholder for shelf-life suitability scoring logic."""
    _ = material, requirements
    return 0.0


def calculate_mechanical_score(material: PackagingMaterial, requirements: PackagingRequirements) -> float:
    """Placeholder for mechanical-fit scoring logic."""
    _ = material, requirements
    return 0.0


def calculate_cost_score(material: PackagingMaterial) -> float:
    """Placeholder for cost scoring logic."""
    _ = material
    return 0.0


def calculate_sustainability_score(material: PackagingMaterial) -> float:
    """Placeholder for sustainability scoring logic."""
    _ = material
    return 0.0


def calculate_overall_score(
    material: PackagingMaterial,
    requirements: PackagingRequirements,
    weights: RankingWeights,
) -> float:
    """Compute weighted overall score with configurable ranking weights."""
    barrier = calculate_barrier_score(material, requirements)
    shelf_life = calculate_shelf_life_score(material, requirements)
    mechanical = calculate_mechanical_score(material, requirements)
    cost = calculate_cost_score(material)
    sustainability = calculate_sustainability_score(material)
    return (
        (barrier * weights.barrier)
        + (shelf_life * weights.shelf_life)
        + (mechanical * weights.mechanical)
        + (cost * weights.cost)
        + (sustainability * weights.sustainability)
    )
