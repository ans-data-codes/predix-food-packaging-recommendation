"""Orchestration layer for end-to-end packaging recommendation flow."""

from src.data.preprocess import prepare_input
from src.data.validators import validate_food_input, validate_storage_conditions
from src.explainability.explanations import (
    explain_recommendation,
    generate_warning_messages,
)
from src.knowledge.rules import apply_domain_rules
from src.packaging_db.material_filters import get_material_candidates
from src.packaging_db.repository import load_packaging_database
from src.ranking.ranking import rank_materials
from src.ranking.weights import RankingWeights
from src.requirements.property_analysis import (
    analyze_food_properties,
    analyze_storage_conditions,
    identify_packaging_drivers,
)
from src.requirements.requirement_derivation import derive_packaging_requirements
from src.schemas.food import FoodInput
from src.schemas.recommendation import RecommendationResult
from src.schemas.storage import StorageConditions
from src.shelf_life.estimator import estimate_shelf_life
from src.sustainability.analysis import calculate_sustainability_score


def recommend_packaging(food: FoodInput, storage: StorageConditions) -> RecommendationResult:
    """Run the modular recommendation pipeline and return a structured result."""
    food = validate_food_input(food)
    storage = validate_storage_conditions(storage)
    food, storage = prepare_input(food, storage)

    food_analysis = analyze_food_properties(food)
    storage_analysis = analyze_storage_conditions(storage)
    drivers = identify_packaging_drivers(food_analysis, storage_analysis)
    requirements = derive_packaging_requirements(drivers)

    materials = load_packaging_database()
    candidates = get_material_candidates(materials, requirements, storage)
    feasible_candidates = apply_domain_rules(requirements, candidates)

    ranked = rank_materials(feasible_candidates, requirements, RankingWeights())
    if not ranked:
        return RecommendationResult(
            material=None,
            reasons=["No feasible materials found with current placeholder rules and data."],
            warnings=generate_warning_messages(),
            alternatives=[],
        )

    material, suitability_score = ranked[0]
    shelf_life_assessment = estimate_shelf_life(material, requirements)

    result = RecommendationResult(
        material=material,
        packaging_structure="to_be_defined",
        suitability_score=suitability_score,
        confidence_score=None,
        recommended_specs={},
        shelf_life_estimate=shelf_life_assessment,
        cost_score=0.0,
        sustainability_score=calculate_sustainability_score(material),
        reasons=[explain_recommendation(material, requirements)],
        warnings=generate_warning_messages(),
        alternatives=[candidate for candidate, _ in ranked[1:4]],
    )
    return result
