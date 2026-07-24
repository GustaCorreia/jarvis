from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel

from app.domain.operations.add_entity_operation import (
    AddEntityOperation,
)
from app.domain.operations.add_relationship_operation import (
    AddRelationshipOperation,
)

from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry

from app.memory.handlers.add_entity_handler import (
    AddEntityHandler,
)
from app.memory.handlers.add_relationship_handler import (
    AddRelationshipHandler,
)


def test_memory_engine_can_learn_relationship():

    world = WorldModel()

    registry = HandlerRegistry()

    registry.register(AddEntityHandler())
    registry.register(AddRelationshipHandler())

    memory = MemoryEngine(registry)

    thor = Entity(
        entity_type=EntityType.UNKNOWN,
    )

    gustavo = Entity(
        entity_type=EntityType.UNKNOWN,
    )

    entity_result = memory.apply(
        AddEntityOperation(thor),
        world,
    )

    assert entity_result.success

    entity_result = memory.apply(
        AddEntityOperation(gustavo),
        world,
    )

    assert entity_result.success

    relationship = Relationship(
        source_entity=thor.id,
        predicate=Predicate.BELONGS_TO,
        target_entity=gustavo.id,
    )

    relationship_result = memory.apply(
        AddRelationshipOperation(relationship),
        world,
    )

    assert relationship_result.success

    assert world.entity_count == 2
    assert world.relationship_count == 1

    relationships = world.find_relationships(
        thor.id,
    )

    assert len(relationships) == 1

    learned = relationships[0]

    assert learned is relationship
    assert learned.source_entity == thor.id
    assert learned.target_entity == gustavo.id
    assert learned.predicate == Predicate.BELONGS_TO
