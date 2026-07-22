from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.world_model import WorldModel

from app.domain.operations.add_entity_operation import (
    AddEntityOperation,
)
from app.domain.operations.add_fact_operation import (
    AddFactOperation,
)

from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry

from app.memory.handlers.add_entity_handler import (
    AddEntityHandler,
)
from app.memory.handlers.add_fact_handler import (
    AddFactHandler,
)


def test_memory_engine_executes_entity_and_fact_operations():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())

    memory = MemoryEngine(registry)

    entity = Entity()

    entity_result = memory.apply(
        AddEntityOperation(entity),
        world,
    )

    assert entity_result.success
    assert world.entity_count == 1
    assert world.contains(entity.id)

    fact = Fact(
        entity_id=entity.id,
        attribute="name",
        value="Thor",
    )

    fact_result = memory.apply(
        AddFactOperation(fact),
        world,
    )

    assert fact_result.success

    facts = world.find_facts(entity.id)

    assert len(facts) == 1
    assert facts[0] is fact
    assert facts[0].attribute == "name"
    assert facts[0].value == "Thor"

    assert world.fact_count == 1
