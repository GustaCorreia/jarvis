from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Confidence:
    """
    Represents a confidence score between 0.0 and 1.0.
    """

    value: float

    def __post_init__(self):
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(
                "Confidence must be between 0.0 and 1.0."
            )

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.2f}"
