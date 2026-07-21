from __future__ import annotations

from pydantic import Field

from app.cognition.core.cognitive_object import CognitiveObject
from app.cognition.emotion.emotion_mention import EmotionMention
from app.cognition.entities.entity_mention import EntityMention
from app.cognition.temporal.date_mention import DateMention
from app.cognition.temporal.time_mention import TimeMention
from app.cognition.understanding.intent_type import IntentType


class Understanding(CognitiveObject):
    """
    Resultado estruturado da interpretação de uma única entrada.

    Este objeto é transitório e representa apenas a compreensão
    da mensagem atual. Cabe ao Learning decidir o que deve ser
    incorporado ao World Model.
    """

    text: str

    intent: IntentType = IntentType.UNKNOWN

    emotion: EmotionMention | None = None

    entities: list[EntityMention] = Field(default_factory=list)

    date: DateMention | None = None

    time: TimeMention | None = None

    confidence: float = 0.0
