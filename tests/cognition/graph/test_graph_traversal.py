from uuid import uuid4

from app.cognition.graph.graph_traversal import GraphTraversal
from app.domain.entity import Entity
from app.domain.predicate import Predicate
from app.domain.relationship import Relationship
from app.domain.world_model import WorldModel


def test_neighbors():

    world = WorldModel()

    gustavo = Entity(
        id=uuid4(),
    )

    thor = Entity(
        id=uuid4(),
    )

    world.add_entity(gustavo)
    world.add_entity(thor)

    world.add_relationship(
        Relationship(
            source_entity=gustavo.id,
            predicate=Predicate.OWNS,
            target_entity=thor.id,
        )
    )

    traversal = GraphTraversal(world)

    neighbors = traversal.neighbors(
        gustavo.id,
    )

    assert len(neighbors) == 1
    assert neighbors[0] == thor
