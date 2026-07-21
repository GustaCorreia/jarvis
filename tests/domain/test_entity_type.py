from app.domain.entity_type import EntityType


def test_entity_type_contains_expected_values():
    assert EntityType.PERSON.value == "person"
    assert EntityType.ANIMAL.value == "animal"
    assert EntityType.PLACE.value == "place"
    assert EntityType.PROJECT.value == "project"
    assert EntityType.DEVICE.value == "device"
    assert EntityType.ORGANIZATION.value == "organization"
    assert EntityType.EVENT.value == "event"
    assert EntityType.UNKNOWN.value == "unknown"
