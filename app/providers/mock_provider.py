from app.providers.base import AIProvider


class MockProvider(AIProvider):
    """
    Provedor temporário utilizado durante o desenvolvimento.
    """

    def generate_response(self, message: str) -> str:
        return (
            "Olá, Senhor. Ainda estou aprendendo sobre você. "
            f"Recebi sua mensagem: '{message}'"
        )
