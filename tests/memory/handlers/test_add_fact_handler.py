from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.operations.add_fact_operation import (
    AddFactOperation,
)
from app.domain.world_model import WorldModel
from app.memory.handlers.add_fact_handler import (
    AddFactHandler,
)


def test_add_fact_handler():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    fact = Fact(
        entity_id=entity.id,
        attribute="name",
        value="Thor",
    )

    handler = AddFactHandler()

    result = handler.handle(
        AddFactOperation(fact),
        world,
    )

    assert result is fact

    stored = world.find_facts(entity.id)

    assert stored == [fact]

    assert world.fact_count == 1
