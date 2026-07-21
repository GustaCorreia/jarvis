from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.has_name_handler import (
    HasNameHandler,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


def test_has_name_creates_operation():
    handler = HasNameHandler()

    fact = Fact(
        subject="Thor",
        predicate=FactPredicate.HAS_NAME,
        value="Thor",
    )

    operations = handler.process(fact)

    assert len(operations) == 1

    operation = operations[0]

    assert operation.operation == KnowledgeOperationType.CREATE_NODE
    assert operation.target == "thor"
    assert operation.payload == {
        "name": "Thor",
    }


def test_process_returns_list():
    handler = HasNameHandler()

    fact = Fact(
        subject="Thor",
        predicate=FactPredicate.HAS_NAME,
        value="Thor",
    )

    operations = handler.process(fact)

    assert isinstance(operations, list)
