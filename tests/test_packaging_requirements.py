from src.schemas.recommendation import PackagingRequirements


def test_packaging_requirements_dataclass_defaults():
    requirements = PackagingRequirements()
    assert isinstance(requirements.special_constraints, list)
    assert requirements.preferred_OTR_range is None
    assert requirements.preferred_WVTR_range is None
