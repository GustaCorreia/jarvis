from uuid import uuid4

from app.cognition.graph.relationship_chain import RelationshipChain
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def connect(
    world: WorldModel,
    source: Entity,
    predicate: Predicate,
    target: Entity,
) -> None:
    world.add_relationship(
        Relationship(
            source_entity=source.id,
            predicate=predicate,
            target_entity=target.id,
        )
    )


def test_relationship_chain_returns_relationships():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, Predicate.OWNS, b)
    connect(world, b, Predicate.LIVES_IN, c)

    chain = RelationshipChain(world)

    result = chain.find(a.id, c.id)

    assert len(result) == 2

    assert result[0].source_entity == a.id
    assert result[0].target_entity == b.id
    assert result[0].predicate == Predicate.OWNS

    assert result[1].source_entity == b.id
    assert result[1].target_entity == c.id
    assert result[1].predicate == Predicate.LIVES_IN


def test_relationship_chain_same_entity():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    chain = RelationshipChain(world)

    assert chain.find(entity.id, entity.id) == []


def test_relationship_chain_without_path():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())

    world.add_entity(a)
    world.add_entity(b)

    chain = RelationshipChain(world)

    assert chain.find(a.id, b.id) == []


def test_relationship_chain_unknown_entity():

    world = WorldModel()

    chain = RelationshipChain(world)

    assert chain.find(uuid4(), uuid4()) == []
