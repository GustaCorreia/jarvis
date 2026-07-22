from app.cognition.knowledge.entity_resolver import (
    EntityResolver,
)
from app.cognition.knowledge.executor import (
    KnowledgeExecutor,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)

from app.domain.world_model import WorldModel

from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry
from app.memory.handlers.add_entity_handler import (
    AddEntityHandler,
)
from app.memory.handlers.add_fact_handler import (
    AddFactHandler,
)


def test_executor_creates_entity_and_fact():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())

    memory = MemoryEngine(registry)

    resolver = EntityResolver(world)

    executor = KnowledgeExecutor(
        memory,
        world,
        resolver,
    )

    operations = [
        KnowledgeOperation(
            operation=KnowledgeOperationType.CREATE_NODE,
            target="thor",
            payload={
                "mention": "Thor",
            },
        )
    ]

    results = executor.execute(operations)

    assert len(results) == 2

    assert results[0].success
    assert results[1].success

    assert world.entity_count == 1
    assert world.fact_count == 1

    entity = world.entities[0]

    facts = world.find_facts(entity.id)

    assert len(facts) == 1
    assert facts[0].attribute == "mention"
    assert facts[0].value == "Thor"


def test_executor_reuses_existing_entity():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())

    memory = MemoryEngine(registry)

    resolver = EntityResolver(world)

    executor = KnowledgeExecutor(
        memory,
        world,
        resolver,
    )

    operation = KnowledgeOperation(
        operation=KnowledgeOperationType.CREATE_NODE,
        target="thor",
        payload={
            "mention": "Thor",
        },
    )

    executor.execute([operation])

    executor.execute([operation])

    assert world.entity_count == 1
    assert world.fact_count == 2

    entity = world.entities[0]

    facts = world.find_facts(entity.id)

    assert len(facts) == 2


def test_empty_operations():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())

    memory = MemoryEngine(registry)

    resolver = EntityResolver(world)

    executor = KnowledgeExecutor(
        memory,
        world,
        resolver,
    )

    results = executor.execute([])

    assert results == []
