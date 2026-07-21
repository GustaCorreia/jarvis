from enum import Enum


class DateType(str, Enum):
    """
    Tipos de referências temporais reconhecidas pelo Jarvis.
    """

    TODAY = "today"

    TOMORROW = "tomorrow"

    YESTERDAY = "yesterday"

    WEEKDAY = "weekday"

    ABSOLUTE_DATE = "absolute_date"

    RELATIVE_DAY = "relative_day"

    RELATIVE_WEEK = "relative_week"

    RELATIVE_MONTH = "relative_month"

    RELATIVE_YEAR = "relative_year"

    UNKNOWN = "unknown"
