from __future__ import annotations

from app.cognition.query.handlers.base_handler import BaseQueryHandler
from app.cognition.query.query import Query
from app.cognition.query.query_result import QueryResult
from app.cognition.query.query_summary import QuerySummary


class GetSummaryHandler(BaseQueryHandler):
    """
    Returns a semantic summary of an entity.
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
            value=QuerySummary(
                entity=entity,
                facts=self._world.find_facts(
                    entity.id
                ),
                relationships=self._world.find_relationships(
                    entity.id
                ),
                neighbors=self._world.neighbors(
                    entity.id
                ),
            ),
        )
