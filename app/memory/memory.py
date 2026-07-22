from __future__ import annotations

from collections.abc import Iterable

from app.domain.fact import Fact


class Memory:
    """
    In-memory storage for facts.
    """

    def __init__(self) -> None:
        self._facts: list[Fact] = []

    def add(self, fact: Fact) -> None:
        self._facts.append(fact)

    def find(
        self,
        subject: str,
        predicate: str,
    ) -> Fact | None:

        for fact in self._facts:

            if (
                fact.subject == subject
                and fact.predicate == predicate
            ):
                return fact

        return None

    def clear(self) -> None:
        self._facts.clear()

    def facts(self) -> Iterable[Fact]:
        return tuple(self._facts)

    def __len__(self) -> int:
        return len(self._facts)
