from app.cognition.query.query import Query
from app.cognition.query.query_engine import KnowledgeQueryEngine
from app.cognition.query.query_type import QueryType

from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.world_model import WorldModel


def build_world():

    world = WorldModel()

    entity = Entity()

    world.add_entity(entity)

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="mention",
            value="thor",
        )
    )

    return world, entity


def test_get_entity():

    world, entity = build_world()

    engine = KnowledgeQueryEngine(world)

    result = engine.execute(
        Query(
            QueryType.GET_ENTITY,
            "thor",
        )
    )

    assert result.success is True

    assert result.value == entity


def test_entity_not_found():

    world = WorldModel()

    engine = KnowledgeQueryEngine(world)

    result = engine.execute(
        Query(
            QueryType.GET_ENTITY,
            "loki",
        )
    )

    assert result.success is False

    assert result.message is not None


def test_get_facts():

    world, entity = build_world()

    world.add_fact(
        Fact(
            entity_id=entity.id,
            attribute="power",
            value="lightning",
        )
    )

    engine = KnowledgeQueryEngine(world)

    result = engine.execute(
        Query(
            QueryType.GET_FACTS,
            "thor",
        )
    )

    assert result.success is True

    assert len(result.value) == 2
