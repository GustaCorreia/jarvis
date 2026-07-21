from app.domain.attribute_type import AttributeType


def test_attribute_types():
    assert AttributeType.STRING.value == "string"
    assert AttributeType.INTEGER.value == "integer"
    assert AttributeType.FLOAT.value == "float"
    assert AttributeType.BOOLEAN.value == "boolean"
