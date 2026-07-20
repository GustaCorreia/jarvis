from __future__ import annotations

from abc import ABC
from typing import Generic

from app.cognition.core.processor import (
    InputT,
    OutputT,
    Processor,
)


class Extractor(
    Processor[InputT, OutputT],
    ABC,
    Generic[InputT, OutputT],
):
    """
    Classe base para todos os extractors da camada
    de Perception.
    """

    pass
