from __future__ import annotations

from app.domain.operations.remove_entity_operation import (
    RemoveEntityOperation,
)
from app.memory.handlers.base_handler import BaseHandler


class RemoveEntityHandler(BaseHandler):
    """
    Handles RemoveEntityOperation.
    """

    @classmethod
    def operation_type(cls):
        return RemoveEntityOperation

    def handle(self, operation, world_model):
        world_model.remove_entity(operation.entity_id)

        return operation.entity_id
