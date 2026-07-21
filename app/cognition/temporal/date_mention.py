from __future__ import annotations

from datetime import date

from pydantic import Field

from app.cognition.core.mention import Mention
from app.cognition.temporal.date_type import DateType


class DateMention(Mention):
    """
    Representa uma referência temporal identificada durante a Percepção.
    """

    date_type: DateType = DateType.UNKNOWN

    normalized: date | None = None

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )
