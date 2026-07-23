from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)
from app.cognition.knowledge.knowledge_planner import (
    KnowledgePlanner,
)


def test_planner_returns_same_operations():

    planner = KnowledgePlanner()

    operations = [
        KnowledgeOperation(
            operation=KnowledgeOperationType.CREATE_NODE,
            target="thor",
            payload={
                "mention": "Thor",
            },
        )
    ]

    plan = planner.build(operations)

    assert len(plan.operations) == 1

    assert plan.operations[0] is operations[0]
