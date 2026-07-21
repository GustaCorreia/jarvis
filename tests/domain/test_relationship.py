from uuid import UUID, uuid4

from app.domain.predicate import Predicate
from app.domain.relationship import Relationship


def test_relationship_creation():
    source = uuid4()
    target = uuid4()

    relationship = Relationship(
        source_entity=source,
        predicate=Predicate.OWNS,
        target_entity=target,
    )

    assert isinstance(relationship.id, UUID)

    assert relationship.source_entity == source

    assert relationship.target_entity == target

    assert relationship.predicate == Predicate.OWNS

    assert relationship.confidence == 1.0

    assert relationship.version == 1
