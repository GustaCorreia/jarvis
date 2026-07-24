from __future__ import annotations

from abc import ABC, abstractmethod

from app.cognition.knowledge.entity_resolver import EntityResolver
from app.cognition.query.query import Query
from app.cognition.query.query_result import QueryResult
from app.domain.entity import Entity
from app.domain.world_model import WorldModel


class BaseQueryHandler(ABC):
    """
    Base class for every semantic query handler.
    Provides common utilities shared by all handlers.
    """

    def __init__(
        self,
        world: WorldModel,
    ) -> None:

        self._world = world
        self._resolver = EntityResolver(world)

    def _resolve_entity(
        self,
        mention: str,
    ) -> Entity | None:
        """
        Resolves a textual mention into an Entity.
        """
        return self._resolver.resolve_by_mention(
            mention
        )

    def _entity_not_found(
        self,
        mention: str,
    ) -> QueryResult:

        return QueryResult(
            success=False,
            message=f"Entity '{mention}' not found.",
        )

    @abstractmethod
    def execute(
        self,
        query: Query,
    ) -> QueryResult:
        """
        Executes a semantic query.
        """
        raise NotImplementedError
