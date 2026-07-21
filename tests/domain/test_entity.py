from datetime import datetime
from uuid import UUID

from app.domain.entity import Entity
from app.domain.entity_type import EntityType


def test_entity_creation():
    entity = Entity(entity_type=EntityType.ANIMAL)

    assert isinstance(entity.id, UUID)
    assert entity.entity_type == EntityType.ANIMAL
    assert entity.version == 1
    assert isinstance(entity.created_at, datetime)
    assert isinstance(entity.updated_at, datetime)


def test_default_entity_type():
    entity = Entity()

    assert entity.entity_type == EntityType.UNKNOWN
