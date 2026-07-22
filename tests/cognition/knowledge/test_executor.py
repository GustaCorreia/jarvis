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


def test_executor_creates_entity():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())

    memory = MemoryEngine(registry)

    executor = KnowledgeExecutor(
        memory,
        world,
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

    assert len(results) == 1

    assert results[0].success

    assert world.entity_count == 1


def test_empty_operations():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())

    memory = MemoryEngine(registry)

    executor = KnowledgeExecutor(
        memory,
        world,
    )

    results = executor.execute([])

    assert results == []
