from datetime import time

from app.cognition.temporal.time_mention import TimeMention
from app.cognition.temporal.time_type import TimeType


def test_create_time_mention():
    mention = TimeMention(
        text="14:30",
        start=0,
        end=5,
        hour=14,
        minute=30,
        normalized=time(14, 30),
        time_type=TimeType.EXACT,
    )

    assert mention.text == "14:30"
    assert mention.hour == 14
    assert mention.minute == 30
    assert mention.normalized == time(14, 30)
    assert mention.time_type == TimeType.EXACT
    assert mention.confidence == 1.0
