from enum import StrEnum


class FactPredicate(StrEnum):
    """
    Predicados canônicos utilizados pelo grafo de conhecimento
    do Jarvis.
    """

    MENTIONS = "mentions"

    IS_A = "is_a"

    HAS_NAME = "has_name"

    HAS_DATE = "has_date"

    HAS_TIME = "has_time"

    LOCATED_AT = "located_at"

    OWNS = "owns"

    BELONGS_TO = "belongs_to"

    RECEIVED = "received"
