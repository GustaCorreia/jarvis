from __future__ import annotations

from app.cognition.core.processor import Processor
from app.cognition.understanding.extractors.entity_extractor import (
    EntityExtractor,
)
from app.cognition.understanding.extractors.intent_extractor import (
    IntentExtractor,
)
from app.cognition.understanding.understanding import Understanding


class UnderstandingProcessor(Processor[str, Understanding]):
    """
    Responsável por transformar uma entrada textual
    em um objeto Understanding.
    """

    def __init__(
        self,
        intent_extractor: IntentExtractor | None = None,
        entity_extractor: EntityExtractor | None = None,
    ) -> None:
        self._intent_extractor = intent_extractor or IntentExtractor()
        self._entity_extractor = entity_extractor or EntityExtractor()

    def process(self, data: str) -> Understanding:
        return Understanding(
            text=data,
            intent=self._intent_extractor.process(data),
            entities=self._entity_extractor.process(data),
        )
