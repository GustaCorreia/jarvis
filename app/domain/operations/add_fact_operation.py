from __future__ import annotations

from dataclasses import dataclass

from app.domain.fact import Fact
from app.domain.operations.base_operation import BaseOperation


@dataclass(frozen=True, slots=True)
class AddFactOperation(BaseOperation):
    """
    Operation that represents adding a Fact
    to the WorldModel.
    """

    fact: Fact
