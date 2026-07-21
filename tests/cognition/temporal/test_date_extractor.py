from app.cognition.temporal.date_extractor import DateExtractor
from app.cognition.temporal.date_type import DateType


extractor = DateExtractor()


def test_detect_today():
    result = extractor.process("Hoje tenho aula.")

    assert len(result) == 1
    assert result[0].date_type == DateType.TODAY


def test_detect_tomorrow():
    result = extractor.process("Amanhã vou ao veterinário.")

    assert len(result) == 1
    assert result[0].date_type == DateType.TOMORROW


def test_detect_yesterday():
    result = extractor.process("Ontem estudei anatomia.")

    assert len(result) == 1
    assert result[0].date_type == DateType.YESTERDAY


def test_multiple_dates():
    result = extractor.process("Hoje estudo e amanhã descanso.")

    assert len(result) == 2
    assert result[0].date_type == DateType.TODAY
    assert result[1].date_type == DateType.TOMORROW


def test_no_dates():
    result = extractor.process("Meu cachorro chama Thor.")

    assert result == []


def test_case_insensitive():
    result = extractor.process("AMANHÃ tenho prova.")

    assert len(result) == 1
    assert result[0].date_type == DateType.TOMORROW


def test_ignore_substring():
    result = extractor.process("hojeeeee")

    assert result == []
