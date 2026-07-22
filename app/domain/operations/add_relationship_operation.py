from __future__ import annotations

from dataclasses import dataclass

from app.domain.operations.base_operation import BaseOperation
from app.domain.relationship import Relationship


@dataclass(frozen=True, slots=True)
class AddRelationshipOperation(BaseOperation):
    """
    Operation that represents adding a relationship
    to the WorldModel.
    """

    relationship: Relationship
