from app.cognition.intent.extractor import IntentExtractor
from app.cognition.models.understanding import Understanding


class UnderstandingEngine:
    """
    Coordena o processo de compreensão da mensagem.

    O motor de compreensão é responsável por transformar
    uma mensagem em um objeto Understanding utilizando
    os diversos processadores cognitivos.
    """

    def __init__(self):

        self.intent_extractor = IntentExtractor()

    def understand(self, message: str) -> Understanding:

        intent = self.intent_extractor.process(message)

        return Understanding(
            intent=intent,
            confidence=1.0,
        )
