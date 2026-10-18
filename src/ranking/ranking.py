"""Candidate ranking interfaces."""

from src.ranking.scoring import calculate_overall_score
from src.ranking.weights import RankingWeights
from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements


def rank_materials(
    materials: list[PackagingMaterial],
    requirements: PackagingRequirements,
    weights: RankingWeights,
) -> list[tuple[PackagingMaterial, float]]:
    """Rank candidate materials by weighted multi-criteria score."""
    scored = [
        (material, calculate_overall_score(material, requirements, weights))
        for material in materials
    ]
    return sorted(scored, key=lambda item: item[1], reverse=True)
