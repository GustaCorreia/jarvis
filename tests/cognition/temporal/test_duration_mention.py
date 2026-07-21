from datetime import timedelta

from app.cognition.temporal.duration_mention import DurationMention
from app.cognition.temporal.duration_type import DurationType


def test_create_duration():
    mention = DurationMention(
        text="2 horas",
        start=0,
        end=7,
        normalized=timedelta(hours=2),
        duration_type=DurationType.RELATIVE,
    )

    assert mention.text == "2 horas"
    assert mention.normalized == timedelta(hours=2)
    assert mention.duration_type == DurationType.RELATIVE
    assert mention.confidence == 1.0
