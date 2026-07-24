from __future__ import annotations

from app.cognition.knowledge.entity_resolver import (
    EntityResolver,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)
from app.cognition.knowledge.knowledge_plan import (
    KnowledgePlan,
)
from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.relationship import Relationship
from app.domain.operations.add_entity_operation import (
    AddEntityOperation,
)
from app.domain.operations.add_fact_operation import (
    AddFactOperation,
)
from app.domain.operations.add_relationship_operation import (
    AddRelationshipOperation,
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
        plan: KnowledgePlan,
    ):
        results = []

        for operation in plan.operations:

            match operation.operation:

                case KnowledgeOperationType.CREATE_NODE:

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

                case KnowledgeOperationType.CREATE_RELATIONSHIP:

                    source_name = operation.payload[
                        "source_entity"
                    ]

                    target_name = operation.payload[
                        "target_entity"
                    ]

                    predicate = operation.payload[
                        "predicate"
                    ]

                    source = (
                        self._resolver.resolve_by_mention(
                            source_name
                        )
                    )

                    target = (
                        self._resolver.resolve_by_mention(
                            target_name
                        )
                    )

                    if source is None:
                        continue

                    if target is None:
                        continue

                    relationship = Relationship(
                        source_entity=source.id,
                        predicate=predicate,
                        target_entity=target.id,
                    )

                    relationship_result = self._memory.apply(
                        AddRelationshipOperation(
                            relationship
                        ),
                        self._world,
                    )

                    results.append(
                        relationship_result
                    )

        return results
