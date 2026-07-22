from __future__ import annotations

from .conversation import Conversation
from .models import Message, Response


class ConversationEngine:
    """
    Coordinates the conversation flow.

    This class is responsible for orchestrating the
    conversation, while Conversation stores the history.
    """

    def __init__(self) -> None:
        self._conversation = Conversation()

    @property
    def conversation(self) -> Conversation:
        return self._conversation

    def receive(self, text: str) -> Response:

        user_message = self._conversation.add_user_message(text)

        response = self._process(user_message)

        self._conversation.add_assistant_message(response.text)

        return response

    def _process(self, message: Message) -> Response:

        normalized = message.text.strip().lower()

        if normalized in {"oi", "olá", "ola"}:
            return Response(
                text="Olá! Como posso ajudar?"
            )

        if normalized in {"tchau", "sair", "exit", "quit"}:
            return Response(
                text="Até logo."
            )

        return Response(
            text="Entendido."
        )
