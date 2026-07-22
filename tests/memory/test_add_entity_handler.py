from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.operations.add_entity_operation import AddEntityOperation
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version
from app.domain.world_model import WorldModel

from app.memory.handlers.add_entity_handler import AddEntityHandler


def make_entity() -> Entity:
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def test_add_entity_handler_adds_entity_to_world():
    world = WorldModel()

    entity = make_entity()

    operation = AddEntityOperation(entity)

    handler = AddEntityHandler()

    result = handler.handle(operation, world)

    assert result == entity
    assert world.entity_count == 1
    assert world.get_entity(entity.id) == entity
