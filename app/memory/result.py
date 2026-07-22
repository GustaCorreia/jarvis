from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class OperationResult:
    """
    Represents the outcome of a memory operation.
    """

    success: bool

    operation: Any

    value: Any = None

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    @property
    def has_warnings(self) -> bool:
        return bool(self.warnings)

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)
