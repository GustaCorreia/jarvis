from app.cognition.understanding.intent_type import IntentType
from app.cognition.understanding.processor import (
    UnderstandingProcessor,
)
from datetime import time


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


def test_process_date():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "Minha consulta será amanhã."
    )

    assert understanding.date is not None


def test_process_time():
    processor = UnderstandingProcessor()

    understanding = processor.process(
        "A consulta será às 14:30."
    )

    assert understanding.time is not None
    assert understanding.time.hour == 14
    assert understanding.time.minute == 30
    assert understanding.time.normalized == time(14, 30)
