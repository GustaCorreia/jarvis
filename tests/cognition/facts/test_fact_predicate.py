from app.cognition.facts.fact_predicate import FactPredicate


def test_mentions():
    assert FactPredicate.MENTIONS == "mentions"


def test_is_a():
    assert FactPredicate.IS_A == "is_a"


def test_received():
    assert FactPredicate.RECEIVED == "received"
