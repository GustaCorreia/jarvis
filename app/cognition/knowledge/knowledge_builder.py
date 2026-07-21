from __future__ import annotations

from app.cognition.facts.fact import Fact
from app.cognition.knowledge.handler_registry import (
    HandlerRegistry,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)


class KnowledgeBuilder:
    """
    Converte Facts em KnowledgeOperations.

    O Builder apenas coordena os componentes.
    Toda a lógica de transformação pertence aos handlers.
    """

    def __init__(self) -> None:
        self._registry = HandlerRegistry()

    def process(
        self,
        facts: list[Fact],
    ) -> list[KnowledgeOperation]:

        operations: list[KnowledgeOperation] = []

        for fact in facts:

            handler = self._registry.get(fact.predicate)

            if handler is None:
                continue

            operations.extend(
                handler.process(fact)
            )

        return operations
