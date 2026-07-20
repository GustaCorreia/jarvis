from enum import StrEnum


class IntentType(StrEnum):
    """
    Representa a intenção identificada em uma entrada.
    """

    UNKNOWN = "unknown"

    INFORM = "inform"

    QUESTION = "question"

    COMMAND = "command"

    GREETING = "greeting"
