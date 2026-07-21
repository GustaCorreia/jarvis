from __future__ import annotations

from datetime import timedelta

from pydantic import Field

from app.cognition.core.mention import Mention
from app.cognition.temporal.duration_type import DurationType


class DurationMention(Mention):
    """
    Representa uma duração identificada durante a percepção.
    """

    duration_type: DurationType = DurationType.UNKNOWN

    normalized: timedelta | None = None

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )
