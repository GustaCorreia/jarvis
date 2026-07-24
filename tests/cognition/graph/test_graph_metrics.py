from uuid import uuid4

from app.cognition.graph.graph_metrics import GraphMetrics
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

    metrics = GraphMetrics(world)

    assert metrics.entity_count() == 0
    assert metrics.relationship_count() == 0
    assert metrics.component_count() == 0
    assert metrics.has_cycles() is False
    assert metrics.is_connected() is True
    assert metrics.average_degree() == 0.0


def test_single_entity():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    metrics = GraphMetrics(world)

    assert metrics.entity_count() == 1
    assert metrics.relationship_count() == 0
    assert metrics.component_count() == 1
    assert metrics.is_connected() is True
    assert metrics.average_degree() == 0.0


def test_connected_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)

    metrics = GraphMetrics(world)

    assert metrics.entity_count() == 3
    assert metrics.relationship_count() == 2
    assert metrics.component_count() == 1
    assert metrics.is_connected() is True
    assert metrics.has_cycles() is False
    assert metrics.average_degree() == 2 / 3


def test_disconnected_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)

    metrics = GraphMetrics(world)

    assert metrics.entity_count() == 3
    assert metrics.relationship_count() == 1
    assert metrics.component_count() == 2
    assert metrics.is_connected() is False


def test_cyclic_graph():

    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    connect(world, a, b)
    connect(world, b, c)
    connect(world, c, a)

    metrics = GraphMetrics(world)

    assert metrics.has_cycles() is True
