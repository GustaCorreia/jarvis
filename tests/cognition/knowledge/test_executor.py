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
from app.cognition.knowledge.knowledge_plan import (
    KnowledgePlan,
)

from app.domain.predicate import Predicate
from app.domain.world_model import WorldModel

from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry
from app.memory.handlers.add_entity_handler import (
    AddEntityHandler,
)
from app.memory.handlers.add_fact_handler import (
    AddFactHandler,
)
from app.memory.handlers.add_relationship_handler import (
    AddRelationshipHandler,
)


def test_executor_creates_entity_and_fact():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())
    registry.register(AddRelationshipHandler())

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

    plan = KnowledgePlan(
        operations=operations,
    )

    results = executor.execute(plan)

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
    registry.register(AddRelationshipHandler())

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

    executor.execute(
        KnowledgePlan(
            operations=[operation],
        )
    )

    executor.execute(
        KnowledgePlan(
            operations=[operation],
        )
    )

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
    registry.register(AddRelationshipHandler())

    memory = MemoryEngine(registry)

    resolver = EntityResolver(world)

    executor = KnowledgeExecutor(
        memory,
        world,
        resolver,
    )

    results = executor.execute(
        KnowledgePlan(
            operations=[],
        )
    )

    assert results == []


def test_executor_creates_relationship():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddFactHandler())
    registry.register(AddRelationshipHandler())

    memory = MemoryEngine(registry)

    resolver = EntityResolver(world)

    executor = KnowledgeExecutor(
        memory,
        world,
        resolver,
    )

    executor.execute(
        KnowledgePlan(
            operations=[
                KnowledgeOperation(
                    operation=KnowledgeOperationType.CREATE_NODE,
                    target="thor",
                    payload={
                        "mention": "Thor",
                    },
                ),
                KnowledgeOperation(
                    operation=KnowledgeOperationType.CREATE_NODE,
                    target="gustavo",
                    payload={
                        "mention": "Gustavo",
                    },
                ),
            ]
        )
    )

    results = executor.execute(
        KnowledgePlan(
            operations=[
                KnowledgeOperation(
                    operation=KnowledgeOperationType.CREATE_RELATIONSHIP,
                    payload={
                        "source_entity": "thor",
                        "target_entity": "gustavo",
                        "predicate": Predicate.BELONGS_TO,
                    },
                )
            ]
        )
    )

    assert len(results) == 1

    assert results[0].success

    assert world.relationship_count == 1

    relationship = world.relationships[0]

    assert (
        relationship.predicate
        == Predicate.BELONGS_TO
    )

    source = world.entities[0]
    target = world.entities[1]

    assert relationship.source_entity == source.id
    assert relationship.target_entity == target.id
