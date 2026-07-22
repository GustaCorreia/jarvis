from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConfidencePolicy:
    """
    Defines how confidence values are evaluated.
    """

    minimum_confidence: float = 0.50

    def accepts(self, confidence: float) -> bool:
        return confidence >= self.minimum_confidence
