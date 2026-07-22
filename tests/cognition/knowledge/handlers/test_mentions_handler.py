from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.mentions_handler import (
    MentionsHandler,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


def test_mentions_creates_operation():
    handler = MentionsHandler()

    fact = Fact(
        subject="message",
        predicate=FactPredicate.MENTIONS,
        value="Thor",
    )

    operations = handler.process(fact)

    assert len(operations) == 1

    operation = operations[0]

    assert operation.operation == KnowledgeOperationType.CREATE_NODE
    assert operation.target == "thor"
    assert operation.payload == {
        "mention": "Thor",
    }
