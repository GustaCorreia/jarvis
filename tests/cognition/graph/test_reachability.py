from uuid import uuid4

from app.cognition.graph.reachability import Reachability
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def connect(
    world: WorldModel,
    source: Entity,
    target: Entity,
) -> None:

    world.add_relationship(
        Relationship(
            source_entity=source.id,
            predicate=Predicate.RELATED_TO,
            target_entity=target.id,
        )
    )


def test_same_entity():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    reachability = Reachability(world)

    assert reachability.exists(entity.id, entity.id)


def test_simple_path():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)

    reachability = Reachability(world)

    assert reachability.exists(a.id, c.id)


def test_unreachable():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())

    world.add_entity(a)
    world.add_entity(b)

    reachability = Reachability(world)

    assert not reachability.exists(a.id, b.id)


def test_unknown_source():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    reachability = Reachability(world)

    assert not reachability.exists(uuid4(), entity.id)


def test_unknown_target():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    reachability = Reachability(world)

    assert not reachability.exists(entity.id, uuid4())


def test_cycle():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)
    connect(world, c, a)

    reachability = Reachability(world)

    assert reachability.exists(a.id, c.id)


def test_branching_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())
    e = Entity(id=uuid4())

    for entity in (a, b, c, d, e):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, a, c)
    connect(world, c, d)
    connect(world, d, e)

    reachability = Reachability(world)

    assert reachability.exists(a.id, e.id)
