from enum import Enum


class AttributeName(str, Enum):
    """
    Canonical names for entity attributes.

    Using an Enum prevents typos and keeps the knowledge model consistent.
    """

    NAME = "name"
    AGE = "age"
    WEIGHT = "weight"
    HEIGHT = "height"
    SPECIES = "species"
    BREED = "breed"
    COLOR = "color"
    EMAIL = "email"
    PHONE = "phone"
