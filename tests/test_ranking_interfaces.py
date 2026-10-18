from src.ranking.ranking import rank_materials
from src.ranking.weights import RankingWeights
from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements


def test_rank_materials_returns_scored_pairs():
    materials = [PackagingMaterial(material_id="m1", material_name="Material 1")]
    ranked = rank_materials(materials, PackagingRequirements(), RankingWeights())
    assert len(ranked) == 1
    assert ranked[0][0].material_id == "m1"
