from __future__ import annotations

from enum import Enum


class Role(str, Enum):
    """
    Represents the author of a message.
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
