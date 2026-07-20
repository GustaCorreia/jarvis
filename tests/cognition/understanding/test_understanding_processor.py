from app.cognition.understanding.intent_type import IntentType
from app.cognition.understanding.processor import (
    UnderstandingProcessor,
)


def test_process_information():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "Meu cachorro Thor tomou vacina."
    )

    assert understanding.text == "Meu cachorro Thor tomou vacina."
    assert understanding.intent == IntentType.INFORM


def test_process_question():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "Quem é você?"
    )

    assert understanding.intent == IntentType.QUESTION


def test_process_greeting():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "Olá Jarvis"
    )

    assert understanding.intent == IntentType.GREETING


def test_process_entities():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "Meu cachorro Thor tomou vacina."
    )

    assert len(understanding.entities) == 1

    entity = understanding.entities[0]

    assert entity.text == "Thor"
    assert entity.entity_type.name == "PET"
