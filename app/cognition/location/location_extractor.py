from __future__ import annotations

import re

from app.cognition.core.processor import Processor
from app.cognition.location.location_mention import LocationMention
from app.cognition.location.location_type import LocationType


class LocationExtractor(Processor[str, list[LocationMention]]):
    """
    Extrai referências simples de localização do texto.
    """

    _KNOWN_LOCATIONS = {
        "casa": LocationType.PLACE,
        "hospital": LocationType.PLACE,
        "clínica": LocationType.PLACE,
        "clinica": LocationType.PLACE,
        "faculdade": LocationType.ORGANIZATION,
        "universidade": LocationType.ORGANIZATION,
        "usp": LocationType.ORGANIZATION,
        "uninove": LocationType.ORGANIZATION,
        "trabalho": LocationType.PLACE,
        "escola": LocationType.ORGANIZATION,
    }

    def process(self, text: str) -> list[LocationMention]:
        mentions: list[LocationMention] = []

        for word, location_type in self._KNOWN_LOCATIONS.items():
            for match in re.finditer(
                rf"\b{re.escape(word)}\b",
                text,
                re.IGNORECASE,
            ):
                mentions.append(
                    LocationMention(
                        text=match.group(),
                        start=match.start(),
                        end=match.end(),
                        location_type=location_type,
                    )
                )

        return mentions
