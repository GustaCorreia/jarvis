from __future__ import annotations


class HandlerRegistry:
    """
    Registry responsible for resolving memory handlers.
    """

    def __init__(self):
        self._handlers = {}

    def register(self, handler):
        self._handlers[handler.operation_type()] = handler

    def get_handler(self, operation):
        return self._handlers.get(type(operation))
