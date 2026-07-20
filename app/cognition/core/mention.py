from __future__ import annotations

from app.cognition.core.cognitive_object import CognitiveObject


class Mention(CognitiveObject):
    """
    Classe base para qualquer evidência produzida pela camada
    de Percepção.

    Uma Mention representa um trecho identificado na entrada,
    mas ainda não corresponde a conhecimento persistente.
    """

    text: str

    start: int = 0

    end: int = 0
