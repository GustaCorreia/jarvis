from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class Processor(ABC, Generic[InputT, OutputT]):
    """
    Classe base para todos os processadores cognitivos.

    Um Processor recebe uma entrada,
    realiza uma transformação
    e devolve uma saída.
    """

    @abstractmethod
    def process(self, data: InputT) -> OutputT:
        """
        Processa a entrada e devolve um resultado.
        """
        raise NotImplementedError
