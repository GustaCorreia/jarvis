from enum import Enum


class DurationType(str, Enum):
    """
    Tipos de duração reconhecidos pelo sistema.
    """

    EXACT = "exact"

    RELATIVE = "relative"

    UNKNOWN = "unknown"
