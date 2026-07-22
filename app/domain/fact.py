from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(slots=True)
class Fact:
    """
    Represents a semantic fact about an entity.

    Example:

        Entity -> Dog

        Fact:
            attribute = "name"
            value = "Thor"
    """

    entity_id: UUID
    attribute: str
    value: object

    id: UUID = field(default_factory=uuid4)
    confidence: float = 1.0
    version: int = 1

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
