from __future__ import annotations

import re

from app.cognition.core.extractor import Extractor
from app.cognition.temporal.date_mention import DateMention
from app.cognition.temporal.date_type import DateType


class DateExtractor(Extractor[str, list[DateMention]]):

    _KEYWORDS = {
        "hoje": DateType.TODAY,
        "amanhã": DateType.TOMORROW,
        "ontem": DateType.YESTERDAY,
    }

    def process(self, data: str) -> list[DateMention]:
        normalized = data.casefold()

        mentions: list[DateMention] = []

        for match in re.finditer(r"\b\w+\b", normalized):
            word = match.group()

            date_type = self._KEYWORDS.get(word)

            if date_type is None:
                continue

            mentions.append(
                DateMention(
                    start=match.start(),
                    end=match.end(),
                    text=data[match.start():match.end()],
                    date_type=date_type,
                )
            )

        return mentions
