from enum import StrEnum


class QueryType(StrEnum):
    """
    Supported query operations for the Knowledge Query Engine.
    """

    GET_ENTITY = "get_entity"

    GET_FACTS = "get_facts"

    GET_RELATIONSHIPS = "get_relationships"

    GET_NEIGHBORS = "get_neighbors"
