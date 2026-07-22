from dataclasses import FrozenInstanceError

import pytest

from app.domain.operations.remove_entity_operation import (
    RemoveEntityOperation,
)
from app.domain.value_objects.entity_id import EntityId


def test_operation_stores_entity_id():
    entity_id = EntityId.generate()

    operation = RemoveEntityOperation(entity_id)

    assert operation.entity_id == entity_id


def test_operation_is_immutable():
    operation = RemoveEntityOperation(EntityId.generate())

    with pytest.raises(FrozenInstanceError):
        operation.entity_id = EntityId.generate()
