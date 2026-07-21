from __future__ import annotations

from abc import ABC, abstractmethod

from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)


class BaseKnowledgeHandler(ABC):
    """
    Classe base para todos os handlers do Knowledge Builder.
    """

    @property
    @abstractmethod
    def predicate(self) -> FactPredicate:
        """
        Predicado suportado pelo handler.
        """
        raise NotImplementedError

    @abstractmethod
    def process(
        self,
        fact: Fact,
    ) -> list[KnowledgeOperation]:
        """
        Converte um Fact em operações de conhecimento.
        """
        raise NotImplementedError
