from app.cognition.temporal.time_type import TimeType


def test_time_type_values():
    assert TimeType.EXACT.value == "exact"
    assert TimeType.RELATIVE.value == "relative"
    assert TimeType.PERIOD.value == "period"
    assert TimeType.UNKNOWN.value == "unknown"
