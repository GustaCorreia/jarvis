from __future__ import annotations

import re

from app.cognition.core.extractor import Extractor
from app.cognition.emotion.emotion_lexicon import EMOTION_KEYWORDS
from app.cognition.emotion.emotion_mention import EmotionMention


class EmotionExtractor(
    Extractor[
        str,
        EmotionMention | None,
    ]
):
    """
    Extrai uma emoção explícita presente no texto.

    Esta classe apenas detecta evidências.
    Ela não interpreta contexto nem realiza inferências.
    """

    DEFAULT_INTENSITY = 0.6

    def process(
        self,
        data: str,
    ) -> EmotionMention | None:

        normalized = data.casefold()

        for match in re.finditer(r"\b\w+\b", normalized):

            token = match.group()

            for emotion_type, keywords in EMOTION_KEYWORDS.items():

                if token in keywords:

                    return EmotionMention(
                        text=data[match.start():match.end()],
                        start=match.start(),
                        end=match.end(),
                        emotion_type=emotion_type,
                        intensity=self.DEFAULT_INTENSITY,
                    )

        return None
