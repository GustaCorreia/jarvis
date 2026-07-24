from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class QueryResult:
    """
    Standard response returned by the KnowledgeQueryEngine.
    """

    success: bool

    value: Any = None

    message: str | None = None
