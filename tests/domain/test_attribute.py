from uuid import UUID, uuid4

from app.domain.attribute import Attribute
from app.domain.attribute_name import AttributeName
from app.domain.attribute_type import AttributeType


def test_attribute_creation():
    entity_id = uuid4()

    attribute = Attribute(
        entity_id=entity_id,
        name=AttributeName.NAME,
        value="Thor",
        value_type=AttributeType.STRING,
    )

    assert isinstance(attribute.id, UUID)
    assert attribute.entity_id == entity_id
    assert attribute.name == AttributeName.NAME
    assert attribute.value == "Thor"
    assert attribute.value_type == AttributeType.STRING
    assert attribute.confidence == 1.0
    assert attribute.version == 1
