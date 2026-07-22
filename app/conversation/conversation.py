from __future__ import annotations

from typing import Iterator

from .models import Message
from .roles import Role


class Conversation:
    """
    Stores the conversation history.

    The Conversation class is responsible only for storing
    exchanged messages. It contains no business logic.
    """

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add_user_message(self, text: str) -> Message:
        message = Message(
            role=Role.USER,
            text=text,
        )

        self._messages.append(message)

        return message

    def add_assistant_message(self, text: str) -> Message:
        message = Message(
            role=Role.ASSISTANT,
            text=text,
        )

        self._messages.append(message)

        return message

    def messages(self) -> tuple[Message, ...]:
        return tuple(self._messages)

    def last_message(self) -> Message | None:
        if not self._messages:
            return None

        return self._messages[-1]

    def clear(self) -> None:
        self._messages.clear()

    def __len__(self) -> int:
        return len(self._messages)

    def __iter__(self) -> Iterator[Message]:
        return iter(self._messages)
