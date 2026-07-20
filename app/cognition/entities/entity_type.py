from enum import StrEnum


class EntityType(StrEnum):
    """
    Tipos de entidades reconhecidas pelo Jarvis.
    """

    UNKNOWN = "unknown"

    PERSON = "person"

    PET = "pet"

    PLACE = "place"

    ORGANIZATION = "organization"

    DEVICE = "device"

    VEHICLE = "vehicle"

    OBJECT = "object"

    CONCEPT = "concept"
