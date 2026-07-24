from __future__ import annotations

from collections import deque
from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class BreadthFirstTraversal(BaseTraversal):
    """
    Performs a Breadth-First Search (BFS) traversal over the WorldModel.

    Entities are visited level by level, starting from the source entity.
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def traverse(self, start: UUID) -> list[Entity]:
        """
        Traverse the graph using Breadth-First Search.

        Args:
            start: Identifier of the starting entity.

        Returns:
            A list of entities in the order they were visited.
        """

        if not self.contains(start):
            return []

        visited: set[UUID] = set()
        queue: deque[UUID] = deque([start])
        result: list[Entity] = []

        while queue:

            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            entity = self.entity(current)
            if entity is not None:
                result.append(entity)

            for neighbor in self.neighbors(current):
                if neighbor.id not in visited:
                    queue.append(neighbor.id)

        return result
