from app.cognition.extractors.intent_extractor import IntentExtractor
from app.cognition.models.understanding import Understanding


class UnderstandingEngine:
    """
    Coordena o processo de compreensão da mensagem.
    """

    def __init__(self):

        self.intent_extractor = IntentExtractor()

    def understand(self, message: str) -> Understanding:

        intent = self.intent_extractor.extract(message)

        return Understanding(
            intent=intent,
            confidence=1.0,
        )
