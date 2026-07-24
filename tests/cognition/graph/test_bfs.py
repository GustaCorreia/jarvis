from uuid import uuid4

from app.cognition.graph.bfs import BreadthFirstTraversal
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def test_bfs_single_node():

    world = WorldModel()

    entity = Entity(id=uuid4())

    world.add_entity(entity)

    bfs = BreadthFirstTraversal(world)

    result = bfs.traverse(entity.id)

    assert result == [entity]


def test_bfs_two_levels():

    world = WorldModel()

    a = Entity(id=uuid4())

    b = Entity(id=uuid4())

    c = Entity(id=uuid4())

    world.add_entity(a)
    world.add_entity(b)
    world.add_entity(c)

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

    bfs = BreadthFirstTraversal(world)

    result = bfs.traverse(a.id)

    assert result == [a, b, c]


def test_bfs_unknown_entity():

    world = WorldModel()

    bfs = BreadthFirstTraversal(world)

    assert bfs.traverse(uuid4()) == []


def test_bfs_cycle():

    world = WorldModel()

    a = Entity(id=uuid4())

    b = Entity(id=uuid4())

    c = Entity(id=uuid4())

    world.add_entity(a)
    world.add_entity(b)
    world.add_entity(c)

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

    bfs = BreadthFirstTraversal(world)

    result = bfs.traverse(a.id)

    assert result == [a, b, c]
