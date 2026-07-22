from __future__ import annotations

from dataclasses import dataclass

from .roles import Role


@dataclass(frozen=True, slots=True)
class Message:
    """
    Represents a message exchanged during a conversation.
    """

    role: Role
    text: str

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Message text cannot be empty.")


@dataclass(frozen=True, slots=True)
class Response:
    """
    Represents Jarvis's response.
    """

    text: str

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Response text cannot be empty.")
