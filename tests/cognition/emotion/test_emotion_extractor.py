from app.cognition.emotion.emotion_type import EmotionType
from app.cognition.emotion.extractor import EmotionExtractor


def test_detects_joy():

    extractor = EmotionExtractor()

    emotion = extractor.process(
        "Estou muito feliz."
    )

    assert emotion is not None
    assert emotion.emotion_type == EmotionType.JOY


def test_detects_sadness():

    extractor = EmotionExtractor()

    emotion = extractor.process(
        "Estou triste."
    )

    assert emotion is not None
    assert emotion.emotion_type == EmotionType.SADNESS


def test_returns_none_when_no_emotion():

    extractor = EmotionExtractor()

    emotion = extractor.process(
        "Hoje está fazendo sol."
    )

    assert emotion is None


def test_case_insensitive():

    extractor = EmotionExtractor()

    emotion = extractor.process(
        "Estou FELIZ!"
    )

    assert emotion is not None
    assert emotion.emotion_type == EmotionType.JOY


def test_does_not_match_substrings():

    extractor = EmotionExtractor()

    emotion = extractor.process(
        "Estou infeliz."
    )

    assert emotion is None
