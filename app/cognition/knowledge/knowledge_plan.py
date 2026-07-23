from __future__ import annotations

from dataclasses import dataclass, field

from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)


@dataclass(slots=True)
class KnowledgePlan:
    """
    Represents a planned set of knowledge operations.

    The planner may later enrich this object with
    confirmations, deferred actions and merge strategies.
    """

    operations: list[KnowledgeOperation] = field(
        default_factory=list
    )
