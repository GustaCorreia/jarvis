from __future__ import annotations

from app.cognition.query.handlers.base_handler import BaseQueryHandler
from app.cognition.query.query import Query
from app.cognition.query.query_result import QueryResult


class GetEntityHandler(BaseQueryHandler):
    """
    Returns a resolved entity.
    """

    def execute(
        self,
        query: Query,
    ) -> QueryResult:

        entity = self._resolve_entity(
            query.entity
        )

        if entity is None:
            return self._entity_not_found(
                query.entity
            )

        return QueryResult(
            success=True,
            value=entity,
        )
