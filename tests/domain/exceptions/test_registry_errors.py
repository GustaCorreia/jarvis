from app.domain.exceptions import (
    DomainError,
    RegistryError,
    DuplicateRegistryItemError,
    RegistryItemNotFoundError,
)


def test_registry_error_inherits_domain_error():
    assert issubclass(RegistryError, DomainError)


def test_duplicate_error_inherits_registry_error():
    assert issubclass(DuplicateRegistryItemError, RegistryError)


def test_not_found_error_inherits_registry_error():
    assert issubclass(RegistryItemNotFoundError, RegistryError)


def test_duplicate_error_message():
    error = DuplicateRegistryItemError("weight")

    assert str(error) == (
        "Registry already contains an item with key 'weight'."
    )


def test_not_found_error_message():
    error = RegistryItemNotFoundError("weight")

    assert str(error) == (
        "No registry item found with key 'weight'."
    )
