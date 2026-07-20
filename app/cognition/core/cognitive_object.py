from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field
from ulid import ULID

from app.shared.time import utc_now


def generate_id() -> str:
    return str(ULID())


class CognitiveObject(BaseModel):
    """
    Classe base para todos os objetos cognitivos do Jarvis.
    """

    id: str = Field(default_factory=generate_id)

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )

    source: str = "system"

    metadata: dict[str, Any] = Field(default_factory=dict)

    created_at: datetime = Field(default_factory=utc_now)

    updated_at: datetime = Field(default_factory=utc_now)
