from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)


def test_operation_values():
    assert (
        KnowledgeOperationType.CREATE_NODE
        == "create_node"
    )

    assert (
        KnowledgeOperationType.UPDATE_NODE
        == "update_node"
    )

    assert (
        KnowledgeOperationType.CREATE_RELATIONSHIP
        == "create_relationship"
    )

    assert (
        KnowledgeOperationType.UPDATE_RELATIONSHIP
        == "update_relationship"
    )
