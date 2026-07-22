from app.domain.operations.add_entity_operation import AddEntityOperation
from app.memory.handler_registry import HandlerRegistry
from app.memory.handlers.add_entity_handler import AddEntityHandler


def test_register_handler():
    registry = HandlerRegistry()

    handler = AddEntityHandler()

    registry.register(handler)

    assert registry.get_handler(AddEntityOperation(None)) is handler
