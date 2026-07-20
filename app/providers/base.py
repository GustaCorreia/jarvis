from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Interface base para qualquer provedor de IA.
    """

    @abstractmethod
    def generate_response(self, message: str) -> str:
        """
        Gera uma resposta para uma mensagem.
        """
        pass
