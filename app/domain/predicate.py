from enum import Enum


class Predicate(str, Enum):
    """
    Canonical predicates used to connect entities
    inside the cognitive world model.
    """

    RELATED_TO = "related_to"

    HAS = "has"

    OWNS = "owns"

    BELONGS_TO = "belongs_to"

    LIVES_IN = "lives_in"

    LOCATED_IN = "located_in"

    WORKS_AT = "works_at"

    STUDIES_AT = "studies_at"

    WORKS_ON = "works_on"

    USES = "uses"

    PART_OF = "part_of"

    KNOWS = "knows"
