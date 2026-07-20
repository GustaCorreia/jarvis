from enum import StrEnum


class EmotionType(StrEnum):
    """
    Emoções básicas reconhecidas pela camada de Percepção.

    Estas emoções representam apenas a classificação inicial
    produzida pelo EmotionExtractor.

    Inferências mais complexas deverão ser realizadas pelas
    camadas posteriores da arquitetura cognitiva.
    """

    UNKNOWN = "unknown"

    NEUTRAL = "neutral"

    JOY = "joy"

    SADNESS = "sadness"

    ANGER = "anger"

    FEAR = "fear"

    SURPRISE = "surprise"

    DISGUST = "disgust"
