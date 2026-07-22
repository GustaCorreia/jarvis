from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class Evidence:
    """
    Represents a single piece of evidence supporting knowledge.
    """

    source: str

    content: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
