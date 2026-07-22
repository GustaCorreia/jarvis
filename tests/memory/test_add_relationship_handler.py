from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.operations.add_relationship_operation import (
    AddRelationshipOperation,
)
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version
from app.domain.world_model import WorldModel

from app.memory.handlers.add_relationship_handler import (
    AddRelationshipHandler,
)


def make_entity() -> Entity:
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def make_relationship():
    source = make_entity()
    target = make_entity()

    relationship = Relationship(
        source_entity=source.id,
        predicate=Predicate.KNOWS,
        target_entity=target.id,
    )

    return relationship, source, target


def test_add_relationship_handler_adds_relationship():
    world = WorldModel()

    relationship, source, target = make_relationship()

    world.add_entity(source)
    world.add_entity(target)

    operation = AddRelationshipOperation(relationship)

    handler = AddRelationshipHandler()

    result = handler.handle(operation, world)

    assert result == relationship

    assert world.relationship_count == 1

    relationships = world.find_relationships(source.id)

    assert relationship in relationships
