"""Prediction interfaces for trained ranking models."""

from typing import Any


def predict_material_score(model: Any, features: Any) -> Any:
    """Predict candidate scores using a trained ranking model."""
    raise NotImplementedError("Model prediction is intentionally not implemented in the architecture stage.")


def save_model(model: Any, path: str) -> None:
    """Persist a trained model artifact to disk."""
    raise NotImplementedError("Model persistence is intentionally not implemented in the architecture stage.")


def load_model(path: str) -> Any:
    """Load a trained model artifact from disk."""
    raise NotImplementedError("Model loading is intentionally not implemented in the architecture stage.")
