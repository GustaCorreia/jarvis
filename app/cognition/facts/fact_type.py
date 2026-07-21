from enum import Enum


class FactType(str, Enum):
    """
    Classifica semanticamente um fato conhecido.
    """

    ATTRIBUTE = "attribute"

    RELATION = "relation"

    EVENT = "event"

    PREFERENCE = "preference"

    UNKNOWN = "unknown"
