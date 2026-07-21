from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.has_name_handler import (
    HasNameHandler,
)


def test_handler_predicate():
    handler = HasNameHandler()

    assert handler.predicate == FactPredicate.HAS_NAME
