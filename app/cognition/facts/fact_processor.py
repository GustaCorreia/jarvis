from __future__ import annotations

from app.cognition.core.processor import Processor
from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.facts.fact_type import FactType
from app.cognition.understanding.understanding import Understanding


class FactProcessor(Processor[Understanding, list[Fact]]):
    """
    Converte um Understanding em uma lista de Facts.
    """

    def process(
        self,
        understanding: Understanding,
    ) -> list[Fact]:
        facts: list[Fact] = []

        #
        # Entity facts
        #
        for entity in understanding.entities:
            facts.append(
                Fact(
                    subject="message",
                    predicate=FactPredicate.MENTIONS,
                    value=entity.text,
                    fact_type=FactType.ATTRIBUTE,
                    confidence=understanding.confidence,
                )
            )

        #
        # Relationship facts
        #
        for relationship in understanding.relationships:
            facts.append(
                Fact(
                    subject=relationship.source,
                    predicate=FactPredicate(
                        relationship.predicate.value
                    ),
                    value=relationship.target,
                    fact_type=FactType.RELATION,
                    confidence=understanding.confidence,
                )
            )

        return facts
