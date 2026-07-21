from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


def test_create_operation():
    operation = KnowledgeOperation(
        operation=KnowledgeOperationType.CREATE_NODE,
        target="thor",
        payload={"name": "Thor"},
    )

    assert operation.operation == KnowledgeOperationType.CREATE_NODE
    assert operation.target == "thor"
    assert operation.payload == {"name": "Thor"}


def test_payload_defaults_to_empty_dict():
    operation = KnowledgeOperation(
        operation=KnowledgeOperationType.UPDATE_NODE,
        target="thor",
    )

    assert operation.payload == {}
