from app.domain.value_objects.entity_id import EntityId


def test_generate_entity_id():
    entity_id = EntityId.generate()

    assert entity_id.value is not None
