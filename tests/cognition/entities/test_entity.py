from app.cognition.entities.entity import Entity
from app.cognition.entities.entity_type import EntityType


def test_create_entity():
    entity = Entity(
        name="Thor",
        type=EntityType.PET,
    )

    assert entity.name == "Thor"
    assert entity.type == EntityType.PET
    assert entity.aliases == []
    assert entity.attributes == {}
