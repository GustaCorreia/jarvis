from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(slots=True)
class ValidationResult:
    """
    Represents the result of a validation process.
    """

    valid: bool = True

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        return bool(self.warnings)


class ValidationRule(ABC):
    """
    Base class for validation rules.
    """

    @abstractmethod
    def validate(self, knowledge, world_model) -> ValidationResult:
        raise NotImplementedError


class ValidationEngine:
    """
    Executes all registered validation rules.
    """

    def __init__(self):
        self._rules: list[ValidationRule] = []

    def register(self, rule: ValidationRule) -> None:
        self._rules.append(rule)

    def validate(self, knowledge, world_model=None) -> ValidationResult:
        result = ValidationResult()

        for rule in self._rules:
            rule_result = rule.validate(knowledge, world_model)

            result.errors.extend(rule_result.errors)
            result.warnings.extend(rule_result.warnings)

        result.valid = not result.has_errors

        return result
