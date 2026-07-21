from enum import Enum


class EntityType(str, Enum):
    """
    Represents the semantic type of an entity.

    The type classifies the entity but does not define its behavior.
    """

    PERSON = "person"
    ANIMAL = "animal"
    PLACE = "place"
    PROJECT = "project"
    DEVICE = "device"
    ORGANIZATION = "organization"
    EVENT = "event"
    UNKNOWN = "unknown"
