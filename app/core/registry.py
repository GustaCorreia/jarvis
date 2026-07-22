from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Iterator, TypeVar

from app.domain.exceptions import (
    DuplicateRegistryItemError,
    RegistryItemNotFoundError,
)

T = TypeVar("T")


class Registry(Generic[T], ABC):
    """
    Generic in-memory registry.

    Concrete registries only need to implement `key_for()`.
    """

    def __init__(self) -> None:
        self._items: Dict[str, T] = {}

    @abstractmethod
    def key_for(self, item: T) -> str:
        """
        Returns the unique key for an item.
        """

    def register(self, item: T) -> None:
        key = self.key_for(item)

        if key in self._items:
            raise DuplicateRegistryItemError(key)

        self._items[key] = item

    def get(self, key: str) -> T:
        try:
            return self._items[key]
        except KeyError:
            raise RegistryItemNotFoundError(key)

    def remove(self, key: str) -> None:
        if key not in self._items:
            raise RegistryItemNotFoundError(key)

        del self._items[key]

    def exists(self, key: str) -> bool:
        return key in self._items

    def clear(self) -> None:
        self._items.clear()

    def keys(self) -> tuple[str, ...]:
        return tuple(self._items.keys())

    def values(self) -> tuple[T, ...]:
        return tuple(self._items.values())

    def items(self) -> tuple[tuple[str, T], ...]:
        return tuple(self._items.items())

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False

        return key in self._items

    def __getitem__(self, key: str) -> T:
        return self.get(key)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items.values())

    def __len__(self) -> int:
        return len(self._items)
