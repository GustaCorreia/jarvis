from __future__ import annotations

from pydantic import Field

from app.cognition.core.mention import Mention
from app.cognition.location.location_type import LocationType


class LocationMention(Mention):
    """
    Representa uma referência espacial encontrada
    durante a percepção.
    """

    location_type: LocationType = LocationType.UNKNOWN

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )
