from __future__ import annotations

from app.conversation.models import Message, Response

from .base import Command


class ExitCommand(Command):

    def execute(self, message: Message) -> Response:

        return Response(
            text="Até logo."
        )
