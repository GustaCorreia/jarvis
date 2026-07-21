from datetime import timedelta

from app.cognition.temporal.duration_extractor import DurationExtractor


def test_extract_hours():
    extractor = DurationExtractor()

    result = extractor.process("Volto em 2 horas.")

    assert len(result) == 1
    assert result[0].normalized == timedelta(hours=2)


def test_extract_minutes():
    extractor = DurationExtractor()

    result = extractor.process("Espere 30 minutos.")

    assert len(result) == 1
    assert result[0].normalized == timedelta(minutes=30)


def test_extract_days():
    extractor = DurationExtractor()

    result = extractor.process("Viajarei por 15 dias.")

    assert len(result) == 1
    assert result[0].normalized == timedelta(days=15)


def test_extract_weeks():
    extractor = DurationExtractor()

    result = extractor.process("Férias de 2 semanas.")

    assert len(result) == 1
    assert result[0].normalized == timedelta(weeks=2)


def test_no_duration():
    extractor = DurationExtractor()

    assert extractor.process("Olá, Jarvis!") == []
