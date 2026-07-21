from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


def test_process_returns_empty_list():
    builder = KnowledgeBuilder()

    operations = builder.process([])

    assert operations == []


def test_unknown_predicate_is_ignored():
    builder = KnowledgeBuilder()

    fact = Fact(
        subject="Thor",
        predicate="unknown",
        value="Thor",
    )

    operations = builder.process([fact])

    assert operations == []


def test_has_name_generates_operation():
    builder = KnowledgeBuilder()

    fact = Fact(
        subject="Thor",
        predicate=FactPredicate.HAS_NAME,
        value="Thor",
    )

    operations = builder.process([fact])

    assert len(operations) == 1

    operation = operations[0]

    assert operation.operation == KnowledgeOperationType.CREATE_NODE
    assert operation.target == "thor"
    assert operation.payload == {
        "name": "Thor",
    }
