from __future__ import annotations

from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.world_model import WorldModel


class CycleDetection(BaseTraversal):
    """
    Detects cycles in the WorldModel graph using
    Depth-First Search (DFS).
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def has_cycle(self) -> bool:
        """
        Returns True if the graph contains at least one cycle.
        """

        visited: set[UUID] = set()
        recursion_stack: set[UUID] = set()

        entities = getattr(self._world, "entities", None)

        if entities is None:
            entities = getattr(self._world, "_entities", {}).values()

        for entity in entities:

            entity_id = entity.id

            if entity_id in visited:
                continue

            if self._visit(
                entity_id,
                visited,
                recursion_stack,
            ):
                return True

        return False

    def _visit(
        self,
        current: UUID,
        visited: set[UUID],
        recursion_stack: set[UUID],
    ) -> bool:
        """
        Recursive DFS used for cycle detection.
        """

        visited.add(current)
        recursion_stack.add(current)

        for neighbor in self.neighbors(current):

            if neighbor.id not in visited:

                if self._visit(
                    neighbor.id,
                    visited,
                    recursion_stack,
                ):
                    return True

            elif neighbor.id in recursion_stack:
                return True

        recursion_stack.remove(current)

        return False

