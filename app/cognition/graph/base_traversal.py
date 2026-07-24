from __future__ import annotations

from uuid import UUID

from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class BaseTraversal:
    """
    Base class for all graph traversal algorithms.

    Provides common access to the WorldModel and utility methods
    shared across traversal implementations.
    """

    def __init__(self, world: WorldModel):
        self._world = world

    def contains(self, entity_id: UUID) -> bool:
        """
        Returns True if the entity exists in the graph.
        """
        return self._world.contains(entity_id)

    def entity(self, entity_id: UUID) -> Entity | None:
        """
        Returns an entity by its identifier.
        """
        return self._world.get_entity(entity_id)

    def neighbors(self, entity_id: UUID) -> list[Entity]:
        """
        Returns neighboring entities.
        """
        return self._world.neighbors(entity_id)
