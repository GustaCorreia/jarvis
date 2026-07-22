from __future__ import annotations

from app.cognition.understanding.processor import (
    UnderstandingProcessor,
)

from .conversation import Conversation
from .models import Message, Response


class ConversationEngine:
    """
    Coordinates the conversation flow.

    This class orchestrates the conversation while
    Conversation stores the history.
    """

    def __init__(self) -> None:
        self._conversation = Conversation()
        self._understanding = UnderstandingProcessor()

    @property
    def conversation(self) -> Conversation:
        return self._conversation

    def receive(self, text: str) -> Response:

        user_message = self._conversation.add_user_message(text)

        understanding = self._understanding.process(
            user_message.text
        )

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

        normalized = message.text.strip().lower()

        #
        # Nesta sprint ainda manteremos
        # o comportamento antigo.
        #

        if normalized in {"oi", "olá", "ola"}:
            return Response(
                text="Olá! Como posso ajudar?"
            )

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
