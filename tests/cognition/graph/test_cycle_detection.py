from uuid import uuid4

from app.cognition.graph.cycle_detection import CycleDetection
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


def test_empty_graph():

    world = WorldModel()

    detector = CycleDetection(world)

    assert detector.has_cycle() is False


def test_single_entity():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    detector = CycleDetection(world)

    assert detector.has_cycle() is False


def test_linear_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)

    detector = CycleDetection(world)

    assert detector.has_cycle() is False


def test_simple_cycle():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)
    connect(world, c, a)

    detector = CycleDetection(world)

    assert detector.has_cycle() is True


def test_disconnected_graph_without_cycle():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())

    for entity in (a, b, c, d):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, c, d)

    detector = CycleDetection(world)

    assert detector.has_cycle() is False


def test_disconnected_graph_with_cycle():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())
    e = Entity(id=uuid4())

    for entity in (a, b, c, d, e):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, c, d)
    connect(world, d, e)
    connect(world, e, c)

    detector = CycleDetection(world)

    assert detector.has_cycle() is True


def test_self_loop():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    connect(world, entity, entity)

    detector = CycleDetection(world)

    assert detector.has_cycle() is True
