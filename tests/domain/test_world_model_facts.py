from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.world_model import WorldModel


def test_world_model_stores_facts():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    fact = Fact(
        entity_id=entity.id,
        attribute="name",
        value="Thor",
    )

    world.add_fact(fact)

    assert world.fact_count == 1

    facts = world.find_facts(entity.id)

    assert facts == [fact]


def test_world_model_clear_removes_facts():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="name",
            value="Thor",
        )
    )

    world.clear()

    assert world.fact_count == 0


def test_remove_entity_removes_associated_facts():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="species",
            value="Dog",
        )
    )

    world.remove_entity(entity.id)

    assert world.fact_count == 0
    assert not world.contains(entity.id)
