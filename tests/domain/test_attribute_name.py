from app.domain.attribute_name import AttributeName


def test_attribute_names():
    assert AttributeName.NAME.value == "name"
    assert AttributeName.AGE.value == "age"
    assert AttributeName.WEIGHT.value == "weight"
    assert AttributeName.SPECIES.value == "species"
