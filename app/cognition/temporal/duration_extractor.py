from __future__ import annotations

import re
from datetime import timedelta

from app.cognition.core.extractor import Extractor
from app.cognition.temporal.duration_mention import DurationMention
from app.cognition.temporal.duration_type import DurationType


class DurationExtractor(Extractor[str, list[DurationMention]]):
    """
    Extrai durações simples em linguagem natural.
    """

    _PATTERN = re.compile(
        r"\b(?P<value>\d+)\s*"
        r"(?P<unit>segundo|segundos|minuto|minutos|hora|horas|dia|dias|semana|semanas)\b",
        re.IGNORECASE,
    )

    def process(self, data: str) -> list[DurationMention]:
        mentions: list[DurationMention] = []

        for match in self._PATTERN.finditer(data):
            value = int(match.group("value"))
            unit = match.group("unit").casefold()

            normalized = self._to_timedelta(value, unit)

            mentions.append(
                DurationMention(
                    text=match.group(0),
                    start=match.start(),
                    end=match.end(),
                    normalized=normalized,
                    duration_type=DurationType.RELATIVE,
                    confidence=1.0,
                )
            )

        return mentions

    @staticmethod
    def _to_timedelta(value: int, unit: str) -> timedelta:
        if unit.startswith("segundo"):
            return timedelta(seconds=value)

        if unit.startswith("minuto"):
            return timedelta(minutes=value)

        if unit.startswith("hora"):
            return timedelta(hours=value)

        if unit.startswith("dia"):
            return timedelta(days=value)

        if unit.startswith("semana"):
            return timedelta(weeks=value)

        raise ValueError(f"Unidade não suportada: {unit}")
