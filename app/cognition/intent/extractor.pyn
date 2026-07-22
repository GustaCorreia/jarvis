from __future__ import annotations

from app.cognition.core.processor import Processor
from app.cognition.understanding.intent_type import IntentType


class IntentExtractor(Processor[str, IntentType]):
    """
    Extrai a intenção principal de um texto.

    Esta implementação utiliza regras simples.
    Futuramente poderá ser substituída por um LLM
    ou outro classificador sem alterar a interface.
    """

    def process(self, data: str) -> IntentType:
        text = data.strip().lower()

        if not text:
            return IntentType.UNKNOWN

        greetings = (
            "oi",
            "olá",
            "ola",
            "bom dia",
            "boa tarde",
            "boa noite",
        )

        if text.startswith(greetings):
            return IntentType.GREETING

        question_words = (
            "quem",
            "qual",
            "quais",
            "como",
            "quando",
            "onde",
            "por que",
            "porque",
        )

        if text.startswith(question_words) or text.endswith("?"):
            return IntentType.QUESTION

        command_words = (
            "abra",
            "feche",
            "ligue",
            "desligue",
            "lembre",
            "crie",
            "execute",
        )

        if text.startswith(command_words):
            return IntentType.COMMAND

        return IntentType.INFORM
