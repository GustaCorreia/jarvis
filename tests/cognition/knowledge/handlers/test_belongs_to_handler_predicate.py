from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.belongs_to_handler import (
    BelongsToHandler,
)


def test_predicate():
    handler = BelongsToHandler()

    assert handler.predicate == FactPredicate.BELONGS_TO
