from app.cognition.knowledge.entity_resolver import (
    EntityResolver,
)
from app.cognition.knowledge.knowledge_operation import (
    KnowledgeOperation,
)
from app.cognition.knowledge.knowledge_operation_type import (
    KnowledgeOperationType,
)

from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.world_model import WorldModel


def make_operation(mention: str):

    return KnowledgeOperation(
        operation=KnowledgeOperationType.CREATE_NODE,
        target=mention.lower(),
        payload={
            "mention": mention,
        },
    )


def test_returns_none_when_world_is_empty():

    world = WorldModel()

    resolver = EntityResolver(world)

    entity = resolver.resolve(
        make_operation("Thor")
    )

    assert entity is None


def test_finds_entity_by_mention():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="mention",
            value="Thor",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("Thor")
    )

    assert result == entity


def test_returns_none_when_mention_not_found():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="mention",
            value="Thor",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("Rex")
    )

    assert result is None

def test_matches_case_insensitive():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="mention",
            value="THOR",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("thor")
    )

    assert result == entity


def test_matches_trimmed_mentions():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="mention",
            value=" Thor ",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("thor")
    )

    assert result == entity

def test_finds_entity_by_alias():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="alias",
            value="Totó",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("Totó")
    )

    assert result == entity

def test_alias_is_case_insensitive():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="alias",
            value="  TOTÓ ",
        )
    )

    resolver = EntityResolver(world)

    result = resolver.resolve(
        make_operation("totó")
    )

    assert result == entity
