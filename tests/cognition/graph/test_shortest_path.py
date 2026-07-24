from uuid import uuid4

from app.cognition.graph.shortest_path import ShortestPath
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def connect(world, source, target):

    world.add_relationship(
        Relationship(
            source_entity=source.id,
            predicate=Predicate.RELATED_TO,
            target_entity=target.id,
        )
    )


def test_same_entity():

    world = WorldModel()

    a = Entity(id=uuid4())

    world.add_entity(a)

    path = ShortestPath(world)

    assert path.find(a.id, a.id) == [a]


def test_no_path():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())

    world.add_entity(a)
    world.add_entity(b)

    path = ShortestPath(world)

    assert path.find(a.id, b.id) == []


def test_simple_path():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)

    path = ShortestPath(world)

    assert path.find(a.id, c.id) == [a, b, c]


def test_shortest_path_prefers_shorter_route():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())

    for entity in (a, b, c, d):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)
    connect(world, c, d)

    connect(world, a, d)

    path = ShortestPath(world)

    assert path.find(a.id, d.id) == [a, d]


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

    path = ShortestPath(world)

    assert path.find(a.id, c.id) == [a, b, c]
