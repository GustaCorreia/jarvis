from __future__ import annotations

from datetime import time

from pydantic import Field

from app.cognition.core.mention import Mention
from app.cognition.temporal.time_type import TimeType


class TimeMention(Mention):
    """
    Representa uma referência de horário identificada durante
    a Percepção.
    """

    time_type: TimeType = TimeType.UNKNOWN

    hour: int | None = Field(
        default=None,
        ge=0,
        le=23,
    )

    minute: int | None = Field(
        default=None,
        ge=0,
        le=59,
    )

    normalized: time | None = None

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )
