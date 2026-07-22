from __future__ import annotations

from .models import Message, Response
from .roles import Role


class ConversationEngine:
    """
    First implementation of Jarvis conversation engine.

    This version contains only the basic conversation flow.
    Future versions will integrate MemoryEngine,
    WorldModel and the LLM adapter.
    """

    def receive(self, text: str) -> Response:
        """
        Processes a user message and returns Jarvis's response.
        """

        message = Message(
            role=Role.USER,
            text=text,
        )

        return self._process(message)

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
