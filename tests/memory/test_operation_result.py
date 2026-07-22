from app.memory.result import OperationResult


def test_success_result():
    result = OperationResult(
        success=True,
        operation="fake",
        value=123,
    )

    assert result.success is True
    assert result.value == 123
    assert not result.has_errors
    assert not result.has_warnings


def test_result_with_errors():
    result = OperationResult(
        success=False,
        operation="fake",
        errors=["failure"],
    )

    assert result.has_errors
    assert result.errors == ["failure"]


def test_result_with_warnings():
    result = OperationResult(
        success=True,
        operation="fake",
        warnings=["warning"],
    )

    assert result.has_warnings
    assert result.warnings == ["warning"]
