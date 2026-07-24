from __future__ import annotations

from app.cognition.core.mention import Mention
from app.domain.predicate import Predicate


class RelationshipMention(Mention):
    """
    Representa uma relação semântica identificada durante
    o processamento de uma entrada.

    Assim como EntityMention, uma RelationshipMention ainda
    não faz parte do World Model. Ela representa apenas uma
    evidência produzida pelo pipeline de percepção.
    """

    source: str

    predicate: Predicate

    target: str
