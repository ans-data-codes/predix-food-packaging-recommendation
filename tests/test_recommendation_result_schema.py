from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import RecommendationResult


def test_recommendation_result_schema_fields():
    material = PackagingMaterial(material_id="m1", material_name="Material 1")
    result = RecommendationResult(material=material)
    assert result.material is material
    assert isinstance(result.reasons, list)
    assert isinstance(result.alternatives, list)
