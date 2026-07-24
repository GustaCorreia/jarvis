from app.cognition.query.query_type import QueryType


def test_query_type_values():
    assert QueryType.GET_ENTITY == "get_entity"
    assert QueryType.GET_FACTS == "get_facts"
    assert QueryType.GET_RELATIONSHIPS == "get_relationships"
    assert QueryType.GET_NEIGHBORS == "get_neighbors"
