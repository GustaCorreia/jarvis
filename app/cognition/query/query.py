from dataclasses import dataclass

from app.cognition.query.query_type import QueryType


@dataclass(slots=True, frozen=True)
class Query:
    """
    Represents a semantic query executed against the WorldModel.

    The entity field contains the textual mention provided by the user.
    The KnowledgeQueryEngine is responsible for resolving it into an
    Entity through the EntityResolver.
    """

    type: QueryType

    entity: str
