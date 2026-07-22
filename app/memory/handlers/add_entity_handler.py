from __future__ import annotations

from app.domain.operations.add_entity_operation import AddEntityOperation
from app.memory.handlers.base_handler import BaseHandler


class AddEntityHandler(BaseHandler):
    """
    Handles AddEntityOperation.
    """

    @classmethod
    def operation_type(cls):
        return AddEntityOperation

    def handle(self, operation, world_model):
        world_model.add_entity(operation.entity)
        return operation.entity
