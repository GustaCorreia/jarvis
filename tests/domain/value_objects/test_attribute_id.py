from app.domain.value_objects.attribute_id import AttributeId


def test_generate_attribute_id():
    attribute_id = AttributeId.generate()

    assert attribute_id.value is not None
