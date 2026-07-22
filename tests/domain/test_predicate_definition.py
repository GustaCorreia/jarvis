from dataclasses import FrozenInstanceError

import pytest

from app.domain.predicate_definition import PredicateDefinition
from app.domain.value_type import ValueType


def test_create_predicate_definition():

    predicate = PredicateDefinition(
        name="name",
        value_type=ValueType.STRING,
        multiple=True,
        keep_history=False,
        description="Entity name",
    )

    assert predicate.name == "name"
    assert predicate.value_type == ValueType.STRING
    assert predicate.multiple is True
    assert predicate.keep_history is False
    assert predicate.description == "Entity name"


def test_predicate_equality():

    p1 = PredicateDefinition(
        name="weight",
        value_type=ValueType.FLOAT,
        multiple=True,
        keep_history=True,
    )

    p2 = PredicateDefinition(
        name="weight",
        value_type=ValueType.FLOAT,
        multiple=True,
        keep_history=True,
    )

    assert p1 == p2


def test_predicate_is_immutable():

    predicate = PredicateDefinition(
        name="birth_date",
        value_type=ValueType.DATE,
        multiple=False,
        keep_history=False,
    )

    with pytest.raises(FrozenInstanceError):
        predicate.name = "other"


def test_description_default():

    predicate = PredicateDefinition(
        name="nickname",
        value_type=ValueType.STRING,
        multiple=True,
        keep_history=False,
    )

    assert predicate.description == ""
