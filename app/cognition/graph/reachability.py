from __future__ import annotations

from collections import deque
from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.world_model import WorldModel


class Reachability(BaseTraversal):
    """
    Determines whether a target entity is reachable from
    a source entity using Breadth-First Search.
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def exists(
        self,
        source: UUID,
        target: UUID,
    ) -> bool:
        """
        Returns True if there is a path from source to target.
        """

        if not self.contains(source):
            return False

        if not self.contains(target):
            return False

        if source == target:
            return True

        visited: set[UUID] = {source}

        queue: deque[UUID] = deque([source])

        while queue:

            current = queue.popleft()

            if current == target:
                return True

            for neighbor in self.neighbors(current):

                if neighbor.id in visited:
                    continue

                visited.add(neighbor.id)

                queue.append(neighbor.id)

        return False
