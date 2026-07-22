from dataclasses import FrozenInstanceError

import pytest

from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.operations.add_relationship_operation import (
    AddRelationshipOperation,
)
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version


def make_entity() -> Entity:
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def make_relationship() -> Relationship:
    return Relationship(
        source_entity=make_entity().id,
        predicate=Predicate.KNOWS,
        target_entity=make_entity().id,
    )


def test_operation_stores_relationship():
    relationship = make_relationship()

    operation = AddRelationshipOperation(relationship)

    assert operation.relationship == relationship


def test_operation_is_immutable():
    relationship = make_relationship()

    operation = AddRelationshipOperation(relationship)

    with pytest.raises(FrozenInstanceError):
        operation.relationship = make_relationship()
