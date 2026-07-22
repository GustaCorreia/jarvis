from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.operations.base_operation import BaseOperation
from app.domain.knowledge.evidence import Evidence


@dataclass(slots=True)
class Knowledge:
    """
    Represents a unit of knowledge with supporting evidence.
    """

    operation: BaseOperation

    evidence: list[Evidence] = field(default_factory=list)

    def add_evidence(self, evidence: Evidence) -> None:
        self.evidence.append(evidence)

    @property
    def evidence_count(self) -> int:
        return len(self.evidence)
