from app.cognition.understanding.intent_type import IntentType
from app.cognition.understanding.understanding import Understanding


def test_create_understanding():
    understanding = Understanding(
        text="Meu cachorro Thor tomou vacina."
    )

    assert understanding.text == "Meu cachorro Thor tomou vacina."
    assert understanding.intent == IntentType.UNKNOWN
    assert understanding.emotion == "neutral"
    assert understanding.entities == []
    assert understanding.confidence == 0.0
