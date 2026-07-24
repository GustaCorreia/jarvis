from __future__ import annotations

from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class DepthFirstTraversal(BaseTraversal):
    """
    Performs a Depth-First Search (DFS) traversal over the WorldModel.

    Entities are visited by exploring each branch as deeply as possible
    before backtracking.
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def traverse(self, start: UUID) -> list[Entity]:
        """
        Traverse the graph using Depth-First Search.

        Args:
            start: Identifier of the starting entity.

        Returns:
            A list of entities in the order they were visited.
        """

        if not self.contains(start):
            return []

        visited: set[UUID] = set()
        result: list[Entity] = []

        self._dfs(start, visited, result)

        return result

    def _dfs(
        self,
        current: UUID,
        visited: set[UUID],
        result: list[Entity],
    ) -> None:
        """
        Recursive DFS implementation.
        """

        if current in visited:
            return

        visited.add(current)

        entity = self.entity(current)
        if entity is not None:
            result.append(entity)

        for neighbor in self.neighbors(current):
            self._dfs(
                neighbor.id,
                visited,
                result,
            )
