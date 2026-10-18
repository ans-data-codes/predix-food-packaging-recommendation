"""Configurable weights for multi-criteria scoring."""

from dataclasses import dataclass


@dataclass
class RankingWeights:
    """Configurable criterion weights for overall ranking score."""

    barrier: float = 0.0
    shelf_life: float = 0.0
    mechanical: float = 0.0
    cost: float = 0.0
    sustainability: float = 0.0
