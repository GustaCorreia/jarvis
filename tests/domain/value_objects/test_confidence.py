import pytest

from app.domain.value_objects.confidence import Confidence


def test_valid_confidence():
    confidence = Confidence(0.75)

    assert confidence.value == 0.75


def test_invalid_confidence_above_one():
    with pytest.raises(ValueError):
        Confidence(1.5)


def test_invalid_confidence_below_zero():
    with pytest.raises(ValueError):
        Confidence(-0.1)
