from app.cognition.entities.entity_type import EntityType


def test_entity_type_values():
    assert EntityType.PERSON == "person"
    assert EntityType.PET == "pet"
    assert EntityType.DEVICE == "device"
    assert EntityType.UNKNOWN == "unknown"
