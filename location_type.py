from enum import Enum


class LocationType(str, Enum):
    """
    Tipos de localização reconhecidos pelo sistema.
    """

    PLACE = "place"

    ORGANIZATION = "organization"

    UNKNOWN = "unknown"
