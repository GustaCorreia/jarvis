from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class RelationshipId:
    """
    Strongly typed identifier for Relationship.
    """

    value: UUID

    @classmethod
    def generate(cls) -> "RelationshipId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)
