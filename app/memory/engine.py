from __future__ import annotations

from app.memory.handler_registry import HandlerRegistry
from app.memory.result import OperationResult
from app.memory.validation import ValidationEngine


class MemoryEngine:
    """
    Coordinates validation and execution of memory operations.
    """

    def __init__(
        self,
        registry: HandlerRegistry,
        validation: ValidationEngine | None = None,
    ):
        self._registry = registry
        self._validation = validation or ValidationEngine()

    def apply(self, operation, world_model):
        validation = self._validation.validate(operation, world_model)

        if not validation.valid:
            return OperationResult(
                success=False,
                operation=operation,
                errors=validation.errors,
                warnings=validation.warnings,
            )

        handler = self._registry.get_handler(operation)

        if handler is None:
            return OperationResult(
                success=False,
                operation=operation,
                errors=[
                    f"No handler registered for {type(operation).__name__}"
                ],
            )

        value = handler.handle(operation, world_model)

        return OperationResult(
            success=True,
            operation=operation,
            value=value,
            warnings=validation.warnings,
        )
