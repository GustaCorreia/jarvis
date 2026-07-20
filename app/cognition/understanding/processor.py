from __future__ import annotations

from app.cognition.core.processor import Processor
from app.cognition.understanding.extractors.intent_extractor import (
    IntentExtractor,
)
from app.cognition.understanding.understanding import Understanding


class UnderstandingProcessor(Processor[str, Understanding]):
    """
    Responsável por transformar uma entrada textual
    em um objeto Understanding.

    Nesta primeira versão apenas a intenção é extraída.
    """

    def __init__(
        self,
        intent_extractor: IntentExtractor | None = None,
    ) -> None:
        self._intent_extractor = (
            intent_extractor or IntentExtractor()
        )

    def process(self, data: str) -> Understanding:
        intent = self._intent_extractor.process(data)

        return Understanding(
            text=data,
            intent=intent,
        )
