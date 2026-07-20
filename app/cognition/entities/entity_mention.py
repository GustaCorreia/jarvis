from __future__ import annotations

from app.cognition.core.mention import Mention
from app.cognition.entities.entity_type import EntityType


class EntityMention(Mention):
    """
    Representa uma ocorrência de uma entidade
    encontrada durante o processamento de uma entrada.

    Uma EntityMention ainda não faz parte do World Model.
    Ela é apenas uma evidência produzida pelo pipeline
    de percepção.
    """

    entity_type: EntityType = EntityType.UNKNOWN
