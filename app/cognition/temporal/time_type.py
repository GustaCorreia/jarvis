from enum import Enum


class TimeType(str, Enum):
    """
    Tipos de referências temporais relacionadas a horários.
    """

    EXACT = "exact"

    RELATIVE = "relative"

    PERIOD = "period"

    UNKNOWN = "unknown"
