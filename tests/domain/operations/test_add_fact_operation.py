from app.domain.entity import Entity
from app.domain.fact import Fact
from app.domain.operations.add_fact_operation import (
    AddFactOperation,
)


def test_add_fact_operation():

    entity = Entity()

    fact = Fact(
        entity_id=entity.id,
        attribute="name",
        value="Thor",
    )

    operation = AddFactOperation(fact=fact)

    assert operation.fact is fact
