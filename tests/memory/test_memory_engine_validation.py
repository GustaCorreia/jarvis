from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry
from app.memory.validation import (
    ValidationEngine,
    ValidationResult,
    ValidationRule,
)


class FakeOperation:
    pass


class RejectRule(ValidationRule):
    def validate(self, knowledge, world_model):
        return ValidationResult(
            valid=False,
            errors=["rejected"],
        )


def test_memory_engine_stops_invalid_operation():
    validation = ValidationEngine()
    validation.register(RejectRule())

    engine = MemoryEngine(
        HandlerRegistry(),
        validation,
    )

    result = engine.apply(
        FakeOperation(),
        None,
    )

    assert not result.success
    assert result.errors == ["rejected"]
