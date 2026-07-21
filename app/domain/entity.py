from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4

from app.domain.entity_type import EntityType


@dataclass(slots=True)
class Entity:
    """
    Represents a unique entity in the cognitive world model.

    This class intentionally contains only identity metadata.
    Attributes, relationships and evidence are modeled separately.
    """

    id: UUID = field(default_factory=uuid4)
    entity_type: EntityType = EntityType.UNKNOWN
    version: int = 1
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
