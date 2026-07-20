class IntentExtractor:
    """
    Responsável por identificar a intenção
    principal da mensagem.
    """

    def extract(self, message: str) -> str:

        message = message.strip()

        if not message:
            return "unknown"

        if message.endswith("?"):
            return "question"

        return "inform"
