from __future__ import annotations

from dataclasses import dataclass

from app.domain.operations.base_operation import BaseOperation
from app.domain.value_objects.entity_id import EntityId


@dataclass(frozen=True, slots=True)
class RemoveEntityOperation(BaseOperation):
    """
    Operation that removes an entity from the WorldModel.
    """

    entity_id: EntityId
