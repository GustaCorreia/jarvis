from datetime import time

from app.cognition.temporal.time_extractor import TimeExtractor
from app.cognition.temporal.time_type import TimeType


def test_extract_single_time():
    extractor = TimeExtractor()

    result = extractor.process("A reunião será às 14:30.")

    assert len(result) == 1

    mention = result[0]

    assert mention.text == "14:30"
    assert mention.hour == 14
    assert mention.minute == 30
    assert mention.normalized == time(14, 30)
    assert mention.time_type == TimeType.EXACT


def test_extract_multiple_times():
    extractor = TimeExtractor()

    result = extractor.process("08:00, 12:15 e 23:59")

    assert len(result) == 3


def test_ignore_invalid_times():
    extractor = TimeExtractor()

    result = extractor.process("25:99 99:00 24:60")

    assert result == []
