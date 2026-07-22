from app.conversation.engine import ConversationEngine


class ChatService:
    """
    Serviço responsável por conversar com o Jarvis.

    Todas as interfaces (CLI, API, Web, Android...)
    devem utilizar este serviço.
    """

    def __init__(self):
        self.engine = ConversationEngine()

    def chat(self, message: str) -> str:
        response = self.engine.receive(message)
        return response.text
