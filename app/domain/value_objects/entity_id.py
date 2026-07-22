from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class EntityId:
    """
    Strongly typed identifier for Entity.
    """

    value: UUID

    @classmethod
    def generate(cls) -> "EntityId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)
