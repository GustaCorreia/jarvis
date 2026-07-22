from __future__ import annotations

from app.conversation.models import Message, Response

from .base import Command


class GreetingCommand(Command):

    def execute(self, message: Message) -> Response:

        return Response(
            text="Olá! Como posso ajudar?"
        )
