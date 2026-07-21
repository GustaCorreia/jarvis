from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_type import FactType


def test_create_fact():
    fact = Fact(
        subject="Thor",
        predicate="age",
        value="4",
        fact_type=FactType.ATTRIBUTE,
    )

    assert fact.subject == "Thor"
    assert fact.predicate == "age"
    assert fact.value == "4"
    assert fact.fact_type == FactType.ATTRIBUTE
    assert fact.confidence == 1.0
    assert fact.source == "conversation"
    assert fact.created_at is not None
    assert fact.updated_at is not None
