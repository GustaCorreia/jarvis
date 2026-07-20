from dataclasses import dataclass


@dataclass(frozen=True)
class Identity:
    """
    Representa a identidade permanente do Jarvis.
    """

    name: str
    version: str
    creator: str
    description: str


identity = Identity(
    name="Jarvis",
    version="0.1.0",
    creator="Gustavo",
    description="Assistente pessoal inteligente em evolução contínua."
)
