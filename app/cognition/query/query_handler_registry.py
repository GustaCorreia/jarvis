from __future__ import annotations

from app.cognition.query.handlers.get_entity_handler import GetEntityHandler
from app.cognition.query.handlers.get_facts_handler import GetFactsHandler
from app.cognition.query.handlers.get_neighbors_handler import (
    GetNeighborsHandler,
)
from app.cognition.query.handlers.get_relationships_handler import (
    GetRelationshipsHandler,
)
from app.cognition.query.handlers.get_summary_handler import (
    GetSummaryHandler,
)
from app.cognition.query.query_type import QueryType
from app.domain.world_model import WorldModel


class QueryHandlerRegistry:
    """
    Registry responsible for mapping QueryType
    to the appropriate handler.
    """

    def __init__(
        self,
        world: WorldModel,
    ) -> None:

        self._handlers = {
            QueryType.GET_ENTITY: GetEntityHandler(world),
            QueryType.GET_FACTS: GetFactsHandler(world),
            QueryType.GET_RELATIONSHIPS: GetRelationshipsHandler(world),
            QueryType.GET_NEIGHBORS: GetNeighborsHandler(world),
            QueryType.GET_SUMMARY: GetSummaryHandler(world),
        }

    def get(
        self,
        query_type: QueryType,
    ):
        handler = self._handlers.get(query_type)

        if handler is None:
            raise ValueError(
                f"No handler registered for '{query_type}'."
            )

        return handler
