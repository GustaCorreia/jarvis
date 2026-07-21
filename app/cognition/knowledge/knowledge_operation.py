from dataclasses import dataclass, field
from typing import Any

from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


@dataclass(frozen=True, slots=True)
class KnowledgeOperation:
    operation: KnowledgeOperationType

    target: str

    payload: dict[str, Any] = field(default_factory=dict)
