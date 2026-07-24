from app.cognition.query.query import Query
from app.cognition.query.query_type import QueryType


def test_query_creation():
    query = Query(
        type=QueryType.GET_ENTITY,
        entity="thor",
    )

    assert query.type == QueryType.GET_ENTITY
    assert query.entity == "thor"
