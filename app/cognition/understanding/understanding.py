from __future__ import annotations

from pydantic import Field

from app.cognition.core.cognitive_object import CognitiveObject
from app.cognition.entities.entity_mention import EntityMention
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

    emotion: str = "neutral"

    entities: list[EntityMention] = Field(default_factory=list)

    confidence: float = 0.0
