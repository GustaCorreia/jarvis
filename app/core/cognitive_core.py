from __future__ import annotations

from app.knowledge import KnowledgeBuilder
from app.memory.engine import MemoryEngine
from app.reasoning import ReasoningEngine


class CognitiveCore:
    """
    High-level façade for the Jarvis cognitive subsystem.
    """

    def __init__(
        self,
        world_model,
        memory: MemoryEngine,
        reasoning: ReasoningEngine,
        builder: KnowledgeBuilder,
    ):
        self._world_model = world_model
        self._memory = memory
        self._reasoning = reasoning
        self._builder = builder

    @property
    def world_model(self):
        return self._world_model

    @property
    def memory(self) -> MemoryEngine:
        return self._memory

    @property
    def reasoning(self) -> ReasoningEngine:
        return self._reasoning

    @property
    def builder(self) -> KnowledgeBuilder:
        return self._builder

    def learn(self, operation):
        """
        Learns an already-built operation.
        """
        return self._memory.apply(
            operation,
            self._world_model,
        )

    def learn_entity(self, entity):
        """
        Learns a new entity using the KnowledgeBuilder.
        """
        operation = self._builder.build_add_entity(entity)
        return self.learn(operation)

    def ask_entity(self, entity_id):
        """
        Retrieves an entity through the ReasoningEngine.
        """
        return self._reasoning.entity_by_id(entity_id)
