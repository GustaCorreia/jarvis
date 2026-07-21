from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from app.domain.predicate import Predicate


@dataclass(slots=True)
class Relationship:
    """
    Represents a semantic relationship between two entities.
    """

    source_entity: UUID

    predicate: Predicate

    target_entity: UUID

    id: UUID = field(default_factory=uuid4)

    confidence: float = 1.0

    version: int = 1

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
