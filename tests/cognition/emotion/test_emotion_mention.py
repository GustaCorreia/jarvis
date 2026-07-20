import pytest
from pydantic import ValidationError

from app.cognition.emotion.emotion_mention import EmotionMention
from app.cognition.emotion.emotion_type import EmotionType


def test_create_emotion_mention():
    mention = EmotionMention(
        text="muito feliz",
        emotion_type=EmotionType.JOY,
        intensity=0.9,
        start=10,
        end=21,
    )

    assert mention.text == "muito feliz"
    assert mention.emotion_type == EmotionType.JOY
    assert mention.intensity == 0.9
    assert mention.start == 10
    assert mention.end == 21


def test_default_intensity():
    mention = EmotionMention(
        text="feliz",
        emotion_type=EmotionType.JOY,
    )

    assert mention.intensity == 1.0


def test_invalid_intensity_below_zero():
    with pytest.raises(ValidationError):
        EmotionMention(
            text="feliz",
            emotion_type=EmotionType.JOY,
            intensity=-0.1,
        )


def test_invalid_intensity_above_one():
    with pytest.raises(ValidationError):
        EmotionMention(
            text="feliz",
            emotion_type=EmotionType.JOY,
            intensity=1.1,
        )
