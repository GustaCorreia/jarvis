from __future__ import annotations

from collections import deque
from uuid import UUID

from app.cognition.graph.base_traversal import BaseTraversal
from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class ConnectedComponents(BaseTraversal):
    """
    Finds all connected components in the WorldModel graph.
    """

    def __init__(self, world: WorldModel):
        super().__init__(world)

    def find(self) -> list[list[Entity]]:
        """
        Returns every connected component.
        """

        visited: set[UUID] = set()
        components: list[list[Entity]] = []

        entities = getattr(self._world, "entities", None)

        if entities is None:
            entities = getattr(self._world, "_entities", {}).values()

        for entity in entities:

            if entity.id in visited:
                continue

            component: list[Entity] = []

            queue: deque[UUID] = deque([entity.id])

            visited.add(entity.id)

            while queue:

                current = queue.popleft()

                current_entity = self.entity(current)

                if current_entity is None:
                    continue

                component.append(current_entity)

                for neighbor in self.neighbors(current):

                    if neighbor.id in visited:
                        continue

                    visited.add(neighbor.id)

                    queue.append(neighbor.id)

            components.append(component)

        return components
