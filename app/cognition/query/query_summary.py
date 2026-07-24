from dataclasses import dataclass

from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.relationship import Relationship


@dataclass(slots=True)
class QuerySummary:
    """
    Represents a complete semantic view of an entity.

    It aggregates the entity itself together with all
    known facts, relationships and neighboring entities.
    """

    entity: Entity

    facts: list[Fact]

    relationships: list[Relationship]

    neighbors: list[Entity]
