from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """
    Represents the version of a domain object.
    """

    value: int = 1

    def __post_init__(self):
        if self.value < 1:
            raise ValueError(
                "Version must be greater than or equal to 1."
            )

    def next(self) -> "Version":
        return Version(self.value + 1)

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
