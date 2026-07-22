from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.operations.remove_entity_operation import (
    RemoveEntityOperation,
)
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version
from app.domain.world_model import WorldModel

from app.memory.handlers.remove_entity_handler import (
    RemoveEntityHandler,
)


def make_entity():
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def test_remove_entity_handler_removes_entity():
    world = WorldModel()

    entity = make_entity()

    world.add_entity(entity)

    operation = RemoveEntityOperation(entity.id)

    handler = RemoveEntityHandler()

    result = handler.handle(operation, world)

    assert result == entity.id
    assert world.entity_count == 0
    assert world.get_entity(entity.id) is None
