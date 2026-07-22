from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.relationship import Relationship


@dataclass(slots=True)
class WorldModel:
    """
    In-memory Knowledge Graph.
    """

    _entities: dict = field(default_factory=dict)
    _relationships: dict = field(default_factory=dict)
    _facts: dict = field(default_factory=dict)

    def add_entity(self, entity: Entity) -> None:
        self._entities[entity.id] = entity

    def add_relationship(
        self,
        relationship: Relationship,
    ) -> None:
        self._relationships.setdefault(
            relationship.source_entity,
            [],
        ).append(relationship)

    def add_fact(self, fact: Fact) -> None:
        self._facts.setdefault(
            fact.entity_id,
            [],
        ).append(fact)

    def get_entity(self, entity_id):
        return self._entities.get(entity_id)

    def has_entity(self, entity_id) -> bool:
        return entity_id in self._entities

    def remove_entity(self, entity_id) -> None:
        self._entities.pop(entity_id, None)
        self._relationships.pop(entity_id, None)
        self._facts.pop(entity_id, None)

    def find_relationships(self, entity_id):
        return list(
            self._relationships.get(entity_id, [])
        )

    def find_facts(self, entity_id):
        return list(
            self._facts.get(entity_id, [])
        )

    def neighbors(self, entity_id):
        return [
            self.get_entity(r.target_entity)
            for r in self.find_relationships(entity_id)
            if self.get_entity(r.target_entity) is not None
        ]

    def degree(self, entity_id) -> int:
        return len(
            self.find_relationships(entity_id)
        )

    def contains(self, entity_id) -> bool:
        return self.has_entity(entity_id)

    def clear(self) -> None:
        self._entities.clear()
        self._relationships.clear()
        self._facts.clear()

    @property
    def entities(self):
        return tuple(
            self._entities.values()
        )

    @property
    def relationships(self):
        return tuple(
            relationship
            for group in self._relationships.values()
            for relationship in group
        )

    @property
    def facts(self):
        return tuple(
            fact
            for group in self._facts.values()
            for fact in group
        )

    @property
    def entity_count(self) -> int:
        return len(self._entities)

    @property
    def relationship_count(self) -> int:
        return sum(
            len(group)
            for group in self._relationships.values()
        )

    @property
    def fact_count(self) -> int:
        return sum(
            len(group)
            for group in self._facts.values()
        )
