from app.cognition.query.query import Query
from app.cognition.query.query_handler_registry import (
    QueryHandlerRegistry,
)
from app.cognition.query.query_result import QueryResult
from app.domain.world_model import WorldModel


class KnowledgeQueryEngine:
    """
    Executes semantic queries by delegating execution
    to specialized query handlers.
    """

    def __init__(
        self,
        world_model: WorldModel,
    ) -> None:

        self._registry = QueryHandlerRegistry(
            world_model
        )

    def execute(
        self,
        query: Query,
    ) -> QueryResult:

        handler = self._registry.get(
            query.type
        )

        return handler.execute(query)
