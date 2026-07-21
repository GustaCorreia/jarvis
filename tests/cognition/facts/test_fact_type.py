from app.cognition.facts.fact_type import FactType


def test_fact_type_values():
    assert FactType.ATTRIBUTE.value == "attribute"
    assert FactType.RELATION.value == "relation"
    assert FactType.EVENT.value == "event"
    assert FactType.PREFERENCE.value == "preference"
    assert FactType.UNKNOWN.value == "unknown"
