from app.cognition.query.query_result import QueryResult


def test_query_result_success():
    result = QueryResult(
        success=True,
        value="Thor",
    )

    assert result.success is True
    assert result.value == "Thor"
    assert result.message is None


def test_query_result_failure():
    result = QueryResult(
        success=False,
        message="Entity not found.",
    )

    assert result.success is False
    assert result.value is None
    assert result.message == "Entity not found."
