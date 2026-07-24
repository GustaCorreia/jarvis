from uuid import uuid4

from app.cognition.graph.connected_components import ConnectedComponents
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


def test_empty_graph():

    world = WorldModel()

    finder = ConnectedComponents(world)

    assert finder.find() == []


def test_single_entity():

    world = WorldModel()

    a = Entity(id=uuid4())

    world.add_entity(a)

    finder = ConnectedComponents(world)

    components = finder.find()

    assert len(components) == 1

    assert components[0] == [a]


def test_two_components():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())

    for entity in (a, b, c, d):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, c, d)

    finder = ConnectedComponents(world)

    components = finder.find()

    sizes = sorted(len(component) for component in components)

    assert sizes == [2, 2]


def test_isolated_entity():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)

    finder = ConnectedComponents(world)

    components = finder.find()

    sizes = sorted(len(component) for component in components)

    assert sizes == [1, 2]


def test_linear_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)

    finder = ConnectedComponents(world)

    components = finder.find()

    assert len(components) == 1

    assert len(components[0]) == 3
