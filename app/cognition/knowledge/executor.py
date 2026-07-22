from __future__ import annotations

from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)
from app.domain.entity import Entity
from app.domain.operations.add_entity_operation import (
    AddEntityOperation,
)


class KnowledgeExecutor:
    """
    Executa KnowledgeOperations utilizando o MemoryEngine.

    Atua como uma camada de adaptação entre a cognição
    e o domínio.
    """

    def __init__(
        self,
        memory_engine,
        world_model,
    ):
        self._memory = memory_engine
        self._world = world_model

    def execute(
        self,
        operations: list[KnowledgeOperation],
    ):
        results = []

        for operation in operations:

            if (
                operation.operation
                == KnowledgeOperationType.CREATE_NODE
            ):
                entity = Entity()

                result = self._memory.apply(
                    AddEntityOperation(entity),
                    self._world,
                )

                results.append(result)

        return results
