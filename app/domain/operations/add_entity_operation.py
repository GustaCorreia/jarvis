from __future__ import annotations

from dataclasses import dataclass

from app.domain.entity import Entity
from app.domain.operations.base_operation import BaseOperation


@dataclass(frozen=True, slots=True)
class AddEntityOperation(BaseOperation):
    """
    Operation that represents adding an entity
    to the WorldModel.
    """

    entity: Entity
