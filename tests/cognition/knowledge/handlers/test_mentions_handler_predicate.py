from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.mentions_handler import (
    MentionsHandler,
)


def test_handler_predicate():
    handler = MentionsHandler()

    assert handler.predicate == FactPredicate.MENTIONS
