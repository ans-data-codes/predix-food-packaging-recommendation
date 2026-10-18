"""Evaluation interfaces for ML ranking models."""

from typing import Any


def evaluate_ranking_model(model: Any, validation_data: Any) -> dict[str, Any]:
    """Evaluate a trained ranking model; metrics to be defined later."""
    raise NotImplementedError("Model evaluation is intentionally not implemented in the architecture stage.")
