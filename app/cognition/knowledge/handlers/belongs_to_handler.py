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
from app.domain.predicate import Predicate


class BelongsToHandler(BaseKnowledgeHandler):
    """
    Handler responsável pelo predicado BELONGS_TO.
    """

    @property
    def predicate(self) -> FactPredicate:
        return FactPredicate.BELONGS_TO

    def process(
        self,
        fact: Fact,
    ) -> list[KnowledgeOperation]:

        return [
            KnowledgeOperation(
                operation=KnowledgeOperationType.CREATE_RELATIONSHIP,
                payload={
                    "source_entity": fact.subject.lower(),
                    "target_entity": fact.value.lower(),
                    "predicate": Predicate.BELONGS_TO,
                },
            )
        ]
