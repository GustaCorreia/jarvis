from __future__ import annotations

from app.cognition.understanding.intent_type import IntentType
from app.cognition.understanding.processor import (
    UnderstandingProcessor,
)
from app.core.cognitive_core import CognitiveCore

from .conversation import Conversation
from .models import Message, Response


class ConversationEngine:
    """
    Coordinates the conversation flow.

    This class orchestrates the conversation while
    Conversation stores the history.
    """

    def __init__(
        self,
        cognitive_core: CognitiveCore | None = None,
    ) -> None:
        self._conversation = Conversation()
        self._understanding = UnderstandingProcessor()
        self._cognitive = cognitive_core

    @property
    def conversation(self) -> Conversation:
        return self._conversation

    @property
    def cognitive(self) -> CognitiveCore | None:
        return self._cognitive

    def receive(self, text: str) -> Response:

        user_message = self._conversation.add_user_message(text)

        understanding = self._understanding.process(
            user_message.text
        )

        #
        # Nesta sprint apenas conectamos o
        # CognitiveCore ao fluxo da conversa.
        #
        # O aprendizado automático será
        # implementado na próxima sprint.
        #

        response = self._process(
            user_message,
            understanding,
        )

        self._conversation.add_assistant_message(
            response.text
        )

        return response

    def _process(
        self,
        message: Message,
        understanding,
    ) -> Response:

        #
        # A partir desta sprint a primeira decisão
        # já utiliza a compreensão da mensagem.
        #

        if understanding.intent == IntentType.GREETING:
            return Response(
                text="Olá! Como posso ajudar?"
            )

        normalized = message.text.strip().lower()

        if normalized in {
            "tchau",
            "sair",
            "exit",
            "quit",
        }:
            return Response(
                text="Até logo."
            )

        return Response(
            text="Entendido."
        )
