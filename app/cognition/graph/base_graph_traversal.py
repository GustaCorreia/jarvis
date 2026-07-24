from __future__ import annotations

from app.domain.world_model import WorldModel


class BaseGraphTraversal:
    """
    Base class for graph traversal algorithms.
    """

    def __init__(
        self,
        world: WorldModel,
    ) -> None:

        self._world = world

    def neighbors(
        self,
        entity_id: str,
    ):
        """
        Returns neighboring entities.
        """

        return self._world.neighbors(
            entity_id
        )

    def contains(
        self,
        entity_id: str,
    ) -> bool:

        return self._world.contains(
            entity_id
        )
