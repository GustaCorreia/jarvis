from app.providers.mock_provider import MockProvider


class ChatService:
    """
    Responsável pela conversa com o usuário.
    """

    def __init__(self):
        self.provider = MockProvider()

    def chat(self, message: str) -> str:
        return self.provider.generate_response(message)
