from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handler_registry import (
    HandlerRegistry,
)
from app.cognition.knowledge.handlers.has_name_handler import (
    HasNameHandler,
)


def test_returns_registered_handler():
    registry = HandlerRegistry()

    handler = registry.get(FactPredicate.HAS_NAME)

    assert isinstance(handler, HasNameHandler)


def test_returns_none_for_unknown_predicate():
    registry = HandlerRegistry()

    handler = registry.get("unknown")

    assert handler is None
