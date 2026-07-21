from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any
from uuid import UUID, uuid4

from app.domain.attribute_name import AttributeName
from app.domain.attribute_type import AttributeType


@dataclass(slots=True)
class Attribute:
    """
    Represents one property of an Entity.
    """

    entity_id: UUID

    name: AttributeName

    value: Any

    value_type: AttributeType

    id: UUID = field(default_factory=uuid4)

    confidence: float = 1.0

    source: str = "user"

    version: int = 1

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
