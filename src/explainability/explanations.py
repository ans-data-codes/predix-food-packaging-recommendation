"""Explanation interfaces for recommendation outputs."""

from src.schemas.packaging import PackagingMaterial
from src.schemas.recommendation import PackagingRequirements


def explain_recommendation(material: PackagingMaterial, requirements: PackagingRequirements) -> str:
    """Generate high-level explanation for recommendation rationale."""
    _ = material, requirements
    return (
        "Recommended because the candidate satisfies current feasibility constraints "
        "and aligns with the configured requirement profile."
    )


def get_top_contributors(material: PackagingMaterial) -> list[str]:
    """Return primary contributing factors for recommendation transparency."""
    _ = material
    return ["Barrier fit", "Storage compatibility", "Sustainability considerations"]


def generate_confidence_explanation(confidence_score: float | None) -> str:
    """Explain confidence score interpretation and current limitations."""
    if confidence_score is None:
        return "Confidence is pending validated rule and model calibration."
    return "Confidence reflects current prototype calibration settings."


def generate_warning_messages() -> list[str]:
    """Return non-production and validation warnings for recommendation outputs."""
    return [
        "Prototype output only: not a substitute for expert/laboratory validation.",
        "Scientific thresholds and model calibration are pending verified sources.",
    ]
