from uuid import uuid4

from app.cognition.graph.dfs import DepthFirstTraversal
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def test_dfs_single_node():
    world = WorldModel()

    entity = Entity(id=uuid4())
    world.add_entity(entity)

    dfs = DepthFirstTraversal(world)

    assert dfs.traverse(entity.id) == [entity]


def test_dfs_unknown_entity():
    world = WorldModel()

    dfs = DepthFirstTraversal(world)

    assert dfs.traverse(uuid4()) == []


def test_dfs_linear_graph():
    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    world.add_relationship(
        Relationship(
            source_entity=a.id,
            predicate=Predicate.RELATED_TO,
            target_entity=b.id,
        )
    )

    world.add_relationship(
        Relationship(
            source_entity=b.id,
            predicate=Predicate.RELATED_TO,
            target_entity=c.id,
        )
    )

    dfs = DepthFirstTraversal(world)

    assert dfs.traverse(a.id) == [a, b, c]


def test_dfs_cycle():
    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())

    for entity in (a, b, c):
        world.add_entity(entity)

    world.add_relationship(
        Relationship(
            source_entity=a.id,
            predicate=Predicate.RELATED_TO,
            target_entity=b.id,
        )
    )

    world.add_relationship(
        Relationship(
            source_entity=b.id,
            predicate=Predicate.RELATED_TO,
            target_entity=c.id,
        )
    )

    world.add_relationship(
        Relationship(
            source_entity=c.id,
            predicate=Predicate.RELATED_TO,
            target_entity=a.id,
        )
    )

    dfs = DepthFirstTraversal(world)

    assert dfs.traverse(a.id) == [a, b, c]


def test_dfs_branching_graph():
    world = WorldModel()

    a = Entity(id=uuid4())
    b = Entity(id=uuid4())
    c = Entity(id=uuid4())
    d = Entity(id=uuid4())

    for entity in (a, b, c, d):
        world.add_entity(entity)

    world.add_relationship(
        Relationship(
            source_entity=a.id,
            predicate=Predicate.RELATED_TO,
            target_entity=b.id,
        )
    )

    world.add_relationship(
        Relationship(
            source_entity=b.id,
            predicate=Predicate.RELATED_TO,
            target_entity=d.id,
        )
    )

    world.add_relationship(
        Relationship(
            source_entity=a.id,
            predicate=Predicate.RELATED_TO,
            target_entity=c.id,
        )
    )

    dfs = DepthFirstTraversal(world)

    assert dfs.traverse(a.id) == [a, b, d, c]
