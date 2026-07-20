from typing import Any

from pydantic import Field

from app.cognition.core.cognitive_object import CognitiveObject
from app.cognition.entities.entity_type import EntityType


class Entity(CognitiveObject):
    """
    Representa qualquer elemento identificável do mundo conhecido pelo Jarvis.
    """

    type: EntityType = EntityType.UNKNOWN

    name: str

    aliases: list[str] = Field(default_factory=list)

    description: str | None = None

    attributes: dict[str, Any] = Field(default_factory=dict)
