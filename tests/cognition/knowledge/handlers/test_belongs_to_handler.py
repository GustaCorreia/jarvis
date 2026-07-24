from app.cognition.facts.fact import Fact
from app.cognition.facts.fact_predicate import FactPredicate
from app.cognition.knowledge.handlers.belongs_to_handler import (
    BelongsToHandler,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)
from app.domain.predicate import Predicate


def test_belongs_to_creates_relationship_operation():

    handler = BelongsToHandler()

    fact = Fact(
        subject="Thor",
        predicate=FactPredicate.BELONGS_TO,
        value="Gustavo",
    )

    operations = handler.process(fact)

    assert len(operations) == 1

    operation = operations[0]

    assert (
        operation.operation
        == KnowledgeOperationType.CREATE_RELATIONSHIP
    )

    assert operation.target is None

    assert operation.payload == {
        "source_entity": "thor",
        "target_entity": "gustavo",
        "predicate": Predicate.BELONGS_TO,
    }


def test_process_returns_list():

    handler = BelongsToHandler()

    fact = Fact(
        subject="Thor",
        predicate=FactPredicate.BELONGS_TO,
        value="Gustavo",
    )

    operations = handler.process(fact)

    assert isinstance(operations, list)
