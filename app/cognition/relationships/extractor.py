from __future__ import annotations

import re

from app.cognition.core.processor import Processor
from app.cognition.relationships.relationship_mention import (
    RelationshipMention,
)
from app.domain.predicate import Predicate


class RelationshipExtractor(
    Processor[str, list[RelationshipMention]]
):
    """
    Extrai relacionamentos presentes no texto.

    Esta implementação utiliza regras simples apenas
    para validar a arquitetura.

    Futuramente poderá ser substituída por NLP ou LLM
    sem alterar o restante do pipeline.
    """

    _BELONGS_TO_PATTERNS = (
        r"\b([A-ZÀ-ÖØ-Ý][\w-]*)\s+pertence\s+a[oà]?\s+([A-ZÀ-ÖØ-Ý][\w-]*)",
        r"\b([A-ZÀ-ÖØ-Ý][\w-]*)\s+belongs\s+to\s+([A-ZÀ-ÖØ-Ý][\w-]*)",
    )

    def process(
        self,
        data: str,
    ) -> list[RelationshipMention]:

        mentions: list[RelationshipMention] = []

        for pattern in self._BELONGS_TO_PATTERNS:

            matches = re.finditer(
                pattern,
                data,
                flags=re.IGNORECASE,
            )

            for match in matches:

                mentions.append(
                    RelationshipMention(
                        text=match.group(0),
                        source=match.group(1),
                        predicate=Predicate.BELONGS_TO,
                        target=match.group(2),
                        start=match.start(),
                        end=match.end(),
                    )
                )

        return mentions
