from dataclasses import dataclass


@dataclass
class Entity:
    """
    Representa qualquer entidade reconhecida pelo Jarvis.
    """

    type: str
    value: str
    confidence: float = 1.0
