from __future__ import annotations

from collections import deque
from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class ShortestPath(BaseTraversal):
    """
    Finds the shortest path between two entities in the WorldModel.

    Since the graph is unweighted, Breadth-First Search (BFS) guarantees
    the shortest path.
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def find(
        self,
        source: UUID,
        target: UUID,
    ) -> list[Entity]:
        """
        Find the shortest path between two entities.

        Args:
            source: Starting entity identifier.
            target: Destination entity identifier.

        Returns:
            A list of entities representing the shortest path.
            Returns an empty list if no path exists.
        """

        if not self.contains(source):
            return []

        if not self.contains(target):
            return []

        if source == target:
            entity = self.entity(source)
            return [entity] if entity is not None else []

        queue: deque[UUID] = deque([source])

        visited: set[UUID] = {source}

        previous: dict[UUID, UUID | None] = {
            source: None,
        }

        while queue:

            current = queue.popleft()

            if current == target:
                break

            for neighbor in self.neighbors(current):

                if neighbor.id in visited:
                    continue

                visited.add(neighbor.id)

                previous[neighbor.id] = current

                queue.append(neighbor.id)

        if target not in previous:
            return []

        path: list[Entity] = []

        current: UUID | None = target

        while current is not None:

            entity = self.entity(current)

            if entity is not None:
                path.append(entity)

            current = previous[current]

        path.reverse()

        return path
