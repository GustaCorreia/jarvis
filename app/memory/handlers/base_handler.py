from __future__ import annotations

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """
    Base class for memory handlers.
    """

    @classmethod
    @abstractmethod
    def operation_type(cls):
        """
        Returns the operation handled by this handler.
        """
        raise NotImplementedError

    @abstractmethod
    def handle(self, operation, world_model):
        raise NotImplementedError
