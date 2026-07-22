from app.domain.value_objects.relationship_id import RelationshipId


def test_generate_relationship_id():
    relationship_id = RelationshipId.generate()

    assert relationship_id.value is not None
