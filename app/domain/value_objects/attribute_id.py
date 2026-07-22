from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AttributeId:
    """
    Strongly typed identifier for Attribute.
    """

    value: UUID

    @classmethod
    def generate(cls) -> "AttributeId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)
