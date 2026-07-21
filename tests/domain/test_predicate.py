from app.domain.predicate import Predicate


def test_predicate_values():
    assert Predicate.RELATED_TO.value == "related_to"
    assert Predicate.OWNS.value == "owns"
    assert Predicate.STUDIES_AT.value == "studies_at"
    assert Predicate.WORKS_ON.value == "works_on"
