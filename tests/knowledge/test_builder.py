from app.domain.operations.add_entity_operation import AddEntityOperation
from app.knowledge import KnowledgeBuilder


class FakeEntity:
    pass


def test_builder_creates_add_entity_operation():
    builder = KnowledgeBuilder()

    entity = FakeEntity()

    operation = builder.build_add_entity(entity)

    assert isinstance(operation, AddEntityOperation)
    assert operation.entity is entity
