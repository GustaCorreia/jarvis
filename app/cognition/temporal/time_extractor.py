from __future__ import annotations

import re
from datetime import time

from app.cognition.core.extractor import Extractor
from app.cognition.temporal.time_mention import TimeMention
from app.cognition.temporal.time_type import TimeType


class TimeExtractor(Extractor[str, list[TimeMention]]):
    """
    Extrai horários no formato HH:MM.
    """

    _PATTERN = re.compile(
        r"\b([01]?\d|2[0-3]):([0-5]\d)\b"
    )

    def process(self, data: str) -> list[TimeMention]:
        mentions: list[TimeMention] = []

        for match in self._PATTERN.finditer(data):
            hour = int(match.group(1))
            minute = int(match.group(2))

            mentions.append(
                TimeMention(
                    text=match.group(0),
                    start=match.start(),
                    end=match.end(),
                    hour=hour,
                    minute=minute,
                    normalized=time(hour, minute),
                    time_type=TimeType.EXACT,
                    confidence=1.0,
                )
            )

        return mentions
