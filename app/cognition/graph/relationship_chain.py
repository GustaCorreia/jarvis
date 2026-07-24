from __future__ import annotations

from uuid import UUID

from app.cognition.graph.shortest_path import ShortestPath
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


class RelationshipChain:
    """
    Finds the sequence of relationships connecting two entities.
    """

    def __init__(self, world: WorldModel):
        self._world = world
        self._shortest_path = ShortestPath(world)

    def find(
        self,
        source: UUID,
        target: UUID,
    ) -> list[Relationship]:
        """
        Returns the ordered list of relationships connecting
        the source entity to the target entity.
        """

        entities = self._shortest_path.find(source, target)

        if len(entities) < 2:
            return []

        chain: list[Relationship] = []

        for current, nxt in zip(entities, entities[1:]):

            relationships = self._world.find_relationships(current.id)

            for relationship in relationships:

                if relationship.target_entity == nxt.id:
                    chain.append(relationship)
                    break

        return chain
