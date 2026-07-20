from datetime import UTC, datetime


def utc_now() -> datetime:
    """Retorna a data e hora atual em UTC."""
    return datetime.now(UTC)
