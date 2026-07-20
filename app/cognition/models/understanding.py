from dataclasses import dataclass, field

from app.cognition.models.entity import Entity
from app.cognition.models.fact import Fact


@dataclass
class Understanding:
    """
    Representa tudo o que o Jarvis compreendeu
    sobre uma única interação.
    """

    intent: str = "unknown"

    emotion: str = "neutral"

    entities: list[Entity] = field(default_factory=list)

    facts: list[Fact] = field(default_factory=list)

    confidence: float = 0.0
