"""Training pipeline interfaces for future ML ranking models."""

from typing import Any


def prepare_training_data(dataset: Any) -> Any:
    """Prepare training dataset for ranking-model experiments."""
    return dataset


def build_features(dataset: Any) -> Any:
    """Build model features from curated training data."""
    return dataset


def train_ranking_model(features: Any, labels: Any) -> Any:
    """Train a ranking model; implementation deferred."""
    raise NotImplementedError("Model training is intentionally not implemented in the architecture stage.")
