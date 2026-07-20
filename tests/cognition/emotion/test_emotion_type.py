from app.cognition.emotion.emotion_type import EmotionType


def test_emotion_type_values():
    assert EmotionType.UNKNOWN == "unknown"
    assert EmotionType.NEUTRAL == "neutral"
    assert EmotionType.JOY == "joy"
    assert EmotionType.SADNESS == "sadness"
    assert EmotionType.ANGER == "anger"
    assert EmotionType.FEAR == "fear"
    assert EmotionType.SURPRISE == "surprise"
    assert EmotionType.DISGUST == "disgust"


def test_emotion_type_count():
    assert len(EmotionType) == 8
