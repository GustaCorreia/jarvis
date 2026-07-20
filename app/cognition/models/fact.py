from dataclasses import dataclass

from app.cognition.models.entity import Entity


@dataclass
class Fact:
    """
    Representa um fato aprendido pelo Jarvis.
    """

    subject: Entity
    relation: str
    object: Entity

    confidence: float = 1.0
    confirmed: bool = False
