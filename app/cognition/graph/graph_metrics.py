from __future__ import annotations

from app.cognition.graph.connected_components import ConnectedComponents
from app.cognition.graph.cycle_detection import CycleDetection
from app.domain.world_model import WorldModel


class GraphMetrics:
    """
    Provides high-level statistics about the knowledge graph.
    """

    def __init__(self, world: WorldModel):
        self._world = world

    def entity_count(self) -> int:
        entities = getattr(self._world, "entities", None)

        if entities is None:
            entities = getattr(self._world, "_entities", {}).values()

        return len(list(entities))

    def relationship_count(self) -> int:
        relationships = getattr(self._world, "relationships", None)

        if relationships is None:
            relationships = getattr(self._world, "_relationships", {}).values()

        return len(list(relationships))

    def component_count(self) -> int:
        return len(ConnectedComponents(self._world).find())

    def has_cycles(self) -> bool:
        return CycleDetection(self._world).has_cycle()

    def is_connected(self) -> bool:
        if self.entity_count() == 0:
            return True

        return self.component_count() == 1

    def average_degree(self) -> float:
        entities = self.entity_count()

        if entities == 0:
            return 0.0

        return self.relationship_count() / entities
