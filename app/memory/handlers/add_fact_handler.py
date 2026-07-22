from __future__ import annotations

from app.domain.operations.add_fact_operation import (
    AddFactOperation,
)
from app.memory.handlers.base_handler import BaseHandler


class AddFactHandler(BaseHandler):
    """
    Handles AddFactOperation.
    """

    @classmethod
    def operation_type(cls):
        return AddFactOperation

    def handle(self, operation, world_model):
        world_model.add_fact(operation.fact)
        return operation.fact
