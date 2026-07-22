from app.domain.operations.add_entity_operation import AddEntityOperation
from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry
from app.memory.handlers.add_entity_handler import AddEntityHandler
from app.memory.validation import ValidationEngine


class FakeWorld:
    def add_entity(self, entity):
        pass


def test_memory_engine_executes_handler():
    registry = HandlerRegistry()
    registry.register(AddEntityHandler())

    engine = MemoryEngine(
        registry,
        ValidationEngine(),
    )

    operation = AddEntityOperation(None)

    result = engine.apply(operation, FakeWorld())

    assert result.success
    assert result.value is None
    assert not result.has_errors
