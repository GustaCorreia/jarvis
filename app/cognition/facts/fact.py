from __future__ import annotations

from datetime import UTC, datetime

from pydantic import Field

from app.cognition.core.cognitive_object import CognitiveObject
from app.cognition.facts.fact_type import FactType


class Fact(CognitiveObject):
    """
    Representa um conhecimento estruturado adquirido pelo Jarvis.
    """

    subject: str
    predicate: str
    value: str

    fact_type: FactType = FactType.UNKNOWN

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )

    source: str = "conversation"

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )
