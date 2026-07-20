from __future__ import annotations

from pydantic import Field

from app.cognition.core.mention import Mention
from app.cognition.emotion.emotion_type import EmotionType


class EmotionMention(Mention):
    """
    Representa uma emoção identificada durante a Percepção.

    Uma EmotionMention é apenas uma evidência extraída da entrada.
    Ela ainda não representa conhecimento persistente nem estado
    emocional confirmado do usuário.
    """

    emotion_type: EmotionType = EmotionType.UNKNOWN

    intensity: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )
