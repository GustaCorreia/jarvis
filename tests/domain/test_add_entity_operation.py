from dataclasses import FrozenInstanceError

import pytest

from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.operations.add_entity_operation import AddEntityOperation
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version


def make_entity() -> Entity:
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def test_operation_stores_entity():
    entity = make_entity()

    operation = AddEntityOperation(entity)

    assert operation.entity == entity


def test_operation_is_immutable():
    entity = make_entity()

    operation = AddEntityOperation(entity)

    with pytest.raises(FrozenInstanceError):
        operation.entity = make_entity()
