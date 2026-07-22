from __future__ import annotations

from abc import ABC, abstractmethod

from app.conversation.models import Message, Response


class Command(ABC):
    """
    Base class for all application commands.
    """

    @abstractmethod
    def execute(self, message: Message) -> Response:
        """
        Executes the command.
        """
        raise NotImplementedError
