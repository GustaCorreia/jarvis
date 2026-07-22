from __future__ import annotations

from app.conversation.models import Message, Response

from .base import Command


class UnknownCommand(Command):

    def execute(self, message: Message) -> Response:

        return Response(
            text="Entendido."
        )
