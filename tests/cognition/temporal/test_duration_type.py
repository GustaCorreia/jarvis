from app.cognition.temporal.duration_type import DurationType


def test_duration_type_values():
    assert DurationType.EXACT.value == "exact"
    assert DurationType.RELATIVE.value == "relative"
    assert DurationType.UNKNOWN.value == "unknown"
