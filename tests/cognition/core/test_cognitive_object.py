from app.cognition.core.cognitive_object import CognitiveObject


def test_create_cognitive_object():
    obj = CognitiveObject()

    assert obj.id is not None
    assert obj.confidence == 1.0
    assert obj.source == "system"
    assert obj.metadata == {}
    assert obj.created_at is not None
    assert obj.updated_at is not None
