from app.cognition.understanding.extractors.intent_extractor import (
    IntentExtractor,
)
from app.cognition.understanding.intent_type import IntentType


def test_extract_greeting():
    extractor = IntentExtractor()

    assert extractor.process("Olá Jarvis") == IntentType.GREETING


def test_extract_question():
    extractor = IntentExtractor()

    assert extractor.process("Quem é você?") == IntentType.QUESTION


def test_extract_command():
    extractor = IntentExtractor()

    assert extractor.process("Abra a garagem") == IntentType.COMMAND


def test_extract_information():
    extractor = IntentExtractor()

    assert (
        extractor.process("Meu cachorro Thor tomou vacina.")
        == IntentType.INFORM
    )


def test_extract_unknown():
    extractor = IntentExtractor()

    assert extractor.process("") == IntentType.UNKNOWN
