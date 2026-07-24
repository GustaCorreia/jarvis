from enum import Enum


class QueryType(str, Enum):
    """
    Supported semantic queries.
    """

    GET_ENTITY = "get_entity"

    GET_FACTS = "get_facts"

    GET_RELATIONSHIPS = "get_relationships"

    GET_NEIGHBORS = "get_neighbors"

    GET_SUMMARY = "get_summary"
