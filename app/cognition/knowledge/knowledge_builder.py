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

    O Builder não contém regras de negócio.
    Toda a lógica de transformação pertence aos handlers
    registrados no HandlerRegistry.
    """

    def __init__(self) -> None:
        self._registry = HandlerRegistry()

    def build(
        self,
        facts: list[Fact],
    ) -> list[KnowledgeOperation]:
        """
        Converte uma lista de Facts em KnowledgeOperations.
        """

        operations: list[KnowledgeOperation] = []

        for fact in facts:

            handler = self._registry.get(
                fact.predicate
            )

            if handler is None:
                continue

            operations.extend(
                handler.process(fact)
            )

        return operations

    def process(
        self,
        facts: list[Fact],
    ) -> list[KnowledgeOperation]:
        """
        Alias temporário para manter compatibilidade
        durante a migração da API.
        """

        return self.build(facts)
