from __future__ import annotations

from app.conversation.engine import ConversationEngine
from app.core.cognitive_core import CognitiveCore


class ChatService:
    """
    Serviço responsável por conversar com o Jarvis.

    Todas as interfaces (CLI, API, Web, Android...)
    devem utilizar este serviço.
    """

    def __init__(
        self,
        engine: ConversationEngine | None = None,
        cognitive_core: CognitiveCore | None = None,
    ):
        if engine is None:
            engine = ConversationEngine(
                cognitive_core=cognitive_core
            )

        self._engine = engine

    @property
    def engine(self) -> ConversationEngine:
        return self._engine

    def chat(self, message: str) -> str:
        response = self._engine.receive(message)
        return response.text
