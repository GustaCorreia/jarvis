from __future__ import annotations

from app.domain.operations.add_relationship_operation import (
    AddRelationshipOperation,
)
from app.memory.handlers.base_handler import BaseHandler


class AddRelationshipHandler(BaseHandler):
    """
    Handles AddRelationshipOperation.
    """

    @classmethod
    def operation_type(cls):
        return AddRelationshipOperation

    def handle(self, operation, world_model):
        world_model.add_relationship(operation.relationship)

        return operation.relationship
