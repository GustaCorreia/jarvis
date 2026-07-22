import pytest

from app.domain.value_objects.version import Version


def test_default_version():
    version = Version()

    assert version.value == 1


def test_next_version():
    version = Version(3)

    assert version.next().value == 4


def test_invalid_version():
    with pytest.raises(ValueError):
        Version(0)
