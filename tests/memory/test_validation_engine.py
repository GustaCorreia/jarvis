from app.memory.validation import (
    ValidationEngine,
    ValidationResult,
    ValidationRule,
)


class FakeKnowledge:
    pass


class FakeRule(ValidationRule):

    def validate(self, knowledge, world_model):
        return ValidationResult()


class ErrorRule(ValidationRule):

    def validate(self, knowledge, world_model):
        return ValidationResult(
            valid=False,
            errors=["error"],
        )


def test_validation_engine_without_rules():
    engine = ValidationEngine()

    result = engine.validate(FakeKnowledge())

    assert result.valid
    assert not result.has_errors


def test_validation_engine_with_success_rule():
    engine = ValidationEngine()

    engine.register(FakeRule())

    result = engine.validate(FakeKnowledge())

    assert result.valid


def test_validation_engine_collects_errors():
    engine = ValidationEngine()

    engine.register(ErrorRule())

    result = engine.validate(FakeKnowledge())

    assert not result.valid
    assert result.errors == ["error"]
