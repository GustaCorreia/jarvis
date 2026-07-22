from app.domain.entity import Entity
from app.domain.fact import Fact


def test_fact_creation():

    entity = Entity()

    fact = Fact(
        entity_id=entity.id,
        attribute="name",
        value="Thor",
    )

    assert fact.entity_id == entity.id
    assert fact.attribute == "name"
    assert fact.value == "Thor"
    assert fact.confidence == 1.0
    assert fact.version == 1
