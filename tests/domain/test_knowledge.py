from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.knowledge.evidence import Evidence
from app.domain.knowledge.knowledge import Knowledge
from app.domain.operations.add_entity_operation import AddEntityOperation
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version


def make_entity():
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def test_add_evidence():
    entity = make_entity()

    operation = AddEntityOperation(entity)

    knowledge = Knowledge(operation)

    evidence = Evidence(
        source="user",
        content="Bob nasceu em 2019."
    )

    knowledge.add_evidence(evidence)

    assert knowledge.evidence_count == 1
    assert knowledge.evidence[0] == evidence
