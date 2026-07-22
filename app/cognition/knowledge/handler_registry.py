from __future__ import annotations

from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.base_handler import (
    BaseKnowledgeHandler,
)
from app.cognition.knowledge.handlers.has_name_handler import (
    HasNameHandler,
)
from app.cognition.knowledge.handlers.mentions_handler import (
    MentionsHandler,
)


class HandlerRegistry:
    """
    Registro central dos handlers de conhecimento.

    É responsável por mapear um FactPredicate para
    seu respectivo handler.
    """

    def __init__(self) -> None:
        handlers: list[BaseKnowledgeHandler] = [
            HasNameHandler(),
            MentionsHandler(),
        ]

        self._handlers = {
            handler.predicate: handler
            for handler in handlers
        }

    def get(
        self,
        predicate: FactPredicate | str,
    ) -> BaseKnowledgeHandler | None:
        return self._handlers.get(predicate)
