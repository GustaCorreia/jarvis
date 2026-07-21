from __future__ import annotations

from app.cognition.core.processor import Processor
from app.cognition.emotion.extractor import EmotionExtractor
from app.cognition.entities.extractor import EntityExtractor
from app.cognition.intent.extractor import IntentExtractor
from app.cognition.location.location_extractor import LocationExtractor
from app.cognition.temporal.date_extractor import DateExtractor
from app.cognition.temporal.duration_extractor import DurationExtractor
from app.cognition.temporal.time_extractor import TimeExtractor
from app.cognition.understanding.understanding import Understanding


class UnderstandingProcessor(Processor[str, Understanding]):
    """
    Responsável por transformar uma entrada textual
    em um objeto Understanding.
    """

    def __init__(
        self,
        intent_extractor: IntentExtractor | None = None,
        entity_extractor: EntityExtractor | None = None,
        emotion_extractor: EmotionExtractor | None = None,
        date_extractor: DateExtractor | None = None,
        time_extractor: TimeExtractor | None = None,
        duration_extractor: DurationExtractor | None = None,
        location_extractor: LocationExtractor | None = None,
    ) -> None:
        self._intent_extractor = intent_extractor or IntentExtractor()
        self._entity_extractor = entity_extractor or EntityExtractor()
        self._emotion_extractor = emotion_extractor or EmotionExtractor()
        self._date_extractor = date_extractor or DateExtractor()
        self._time_extractor = time_extractor or TimeExtractor()
        self._duration_extractor = duration_extractor or DurationExtractor()
        self._location_extractor = (
            location_extractor or LocationExtractor()
        )

    def process(self, data: str) -> Understanding:
        return Understanding(
            text=data,
            intent=self._intent_extractor.process(data),
            emotion=self._emotion_extractor.process(data),
            entities=self._entity_extractor.process(data),
            date=self._first_date(data),
            time=self._first_time(data),
            duration=self._first_duration(data),
            location=self._first_location(data),
        )

    def _first_date(self, text: str):
        dates = self._date_extractor.process(text)

        if not dates:
            return None

        return dates[0]

    def _first_time(self, text: str):
        times = self._time_extractor.process(text)

        if not times:
            return None

        return times[0]

    def _first_duration(self, text: str):
        durations = self._duration_extractor.process(text)

        if not durations:
            return None

        return durations[0]

    def _first_location(self, text: str):
        locations = self._location_extractor.process(text)

        if not locations:
            return None

        return locations[0]
