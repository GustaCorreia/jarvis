from __future__ import annotations

from app.cognition.knowledge.knowledge_plan import (
    KnowledgePlan,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)


class KnowledgePlanner:
    """
    Produces an execution plan from knowledge operations.

    Initial implementation:
    simply forwards every operation.
    """

    def build(
        self,
        operations: list[KnowledgeOperation],
    ) -> KnowledgePlan:

        return KnowledgePlan(
            operations=operations.copy()
        )
