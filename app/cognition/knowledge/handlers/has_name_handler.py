from __future__ import annotations

from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.base_handler import (
    BaseKnowledgeHandler,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


class HasNameHandler(BaseKnowledgeHandler):
    """
    Handler responsável pelo predicado HAS_NAME.
    """

    @property
    def predicate(self) -> FactPredicate:
        return FactPredicate.HAS_NAME

    def process(
        self,
        fact: Fact,
    ) -> list[KnowledgeOperation]:

        return [
            KnowledgeOperation(
                operation=KnowledgeOperationType.CREATE_NODE,
                target=fact.subject.lower(),
                payload={
                    "name": fact.value,
                },
            )
        ]
