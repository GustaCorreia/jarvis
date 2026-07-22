from __future__ import annotations

from app.domain.exceptions.domain_error import DomainError


class RegistryError(DomainError):
    """
    Base exception for registry-related errors.
    """

    pass


class DuplicateRegistryItemError(RegistryError):
    """
    Raised when attempting to register an item whose key already exists.
    """

    def __init__(self, key: str):
        self.key = key
        super().__init__(f"Registry already contains an item with key '{key}'.")


class RegistryItemNotFoundError(RegistryError):
    """
    Raised when a requested registry item does not exist.
    """

    def __init__(self, key: str):
        self.key = key
        super().__init__(f"No registry item found with key '{key}'.")
