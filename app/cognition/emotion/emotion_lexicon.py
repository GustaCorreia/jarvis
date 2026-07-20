from __future__ import annotations

from app.cognition.emotion.emotion_type import EmotionType

EMOTION_KEYWORDS: dict[EmotionType, set[str]] = {
    EmotionType.JOY: {
        "feliz",
        "alegre",
        "contente",
        "animado",
    },
    EmotionType.SADNESS: {
        "triste",
        "abatido",
        "deprimido",
    },
    EmotionType.ANGER: {
        "raiva",
        "furioso",
        "irritado",
        "bravo",
    },
    EmotionType.FEAR: {
        "medo",
        "assustado",
        "preocupado",
    },
    EmotionType.SURPRISE: {
        "surpreso",
        "espantado",
    },
    EmotionType.DISGUST: {
        "nojento",
        "repugnante",
    },
}
