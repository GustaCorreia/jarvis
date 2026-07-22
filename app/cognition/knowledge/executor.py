from __future__ import annotations

from app.cognition.knowledge.entity_resolver import (
    EntityResolver,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)
from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.operations.add_entity_operation import (
    AddEntityOperation,
)
from app.domain.operations.add_fact_operation import (
    AddFactOperation,
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
        entity_resolver: EntityResolver,
    ):
        self._memory = memory_engine
        self._world = world_model
        self._resolver = entity_resolver

    def execute(
        self,
        operations: list[KnowledgeOperation],
    ):
        results = []

        for operation in operations:

            if (
                operation.operation
                != KnowledgeOperationType.CREATE_NODE
            ):
                continue

            entity = self._resolver.resolve(operation)

            if entity is None:

                entity = Entity()

                entity_result = self._memory.apply(
                    AddEntityOperation(entity),
                    self._world,
                )

                results.append(entity_result)

                if not entity_result.success:
                    continue

            for attribute, value in operation.payload.items():

                fact = Fact(
                    entity_id=entity.id,
                    attribute=attribute,
                    value=value,
                )

                fact_result = self._memory.apply(
                    AddFactOperation(fact),
                    self._world,
                )

                results.append(fact_result)

        return results
