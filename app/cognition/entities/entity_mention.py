from __future__ import annotations

from app.cognition.core.cognitive_object import CognitiveObject
from app.cognition.entities.entity_type import EntityType


class EntityMention(CognitiveObject):
    """
    Representa uma ocorrência de uma entidade
    encontrada durante o processamento de uma entrada.

    Uma EntityMention ainda não faz parte do World Model.
    Ela é apenas uma evidência produzida pelo pipeline
    de entendimento.
    """

    text: str

    entity_type: EntityType = EntityType.UNKNOWN

    start: int = 0

    end: int = 0
