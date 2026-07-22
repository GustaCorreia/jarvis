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


class MentionsHandler(BaseKnowledgeHandler):
    """
    Handler responsável pelo predicado MENTIONS.
    """

    @property
    def predicate(self) -> FactPredicate:
        return FactPredicate.MENTIONS

    def process(
        self,
        fact: Fact,
    ) -> list[KnowledgeOperation]:

        return [
            KnowledgeOperation(
                operation=KnowledgeOperationType.CREATE_NODE,
                target=fact.value.lower(),
                payload={
                    "mention": fact.value,
                },
            )
        ]
