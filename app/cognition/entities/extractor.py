from __future__ import annotations

import re

from app.cognition.core.processor import Processor
from app.cognition.entities.entity_mention import EntityMention
from app.cognition.entities.entity_type import EntityType


class EntityExtractor(Processor[str, list[EntityMention]]):
    """
    Extrai menções de entidades presentes no texto.

    Esta primeira implementação utiliza regras simples apenas
    para validar a arquitetura do pipeline cognitivo.

    Futuramente esta classe poderá ser substituída por um modelo
    de NLP sem alterar os componentes que a utilizam.
    """

    _PET_PATTERNS: tuple[tuple[str, EntityType], ...] = (
        (r"\bmeu cachorro\s+([A-ZÀ-ÖØ-Ý][\w-]*)", EntityType.PET),
        (r"\bminha cachorra\s+([A-ZÀ-ÖØ-Ý][\w-]*)", EntityType.PET),
        (r"\bmeu gato\s+([A-ZÀ-ÖØ-Ý][\w-]*)", EntityType.PET),
        (r"\bminha gata\s+([A-ZÀ-ÖØ-Ý][\w-]*)", EntityType.PET),
    )

    def process(self, data: str) -> list[EntityMention]:
        """
        Extrai todas as menções de entidades encontradas no texto.

        Parameters
        ----------
        data:
            Texto de entrada.

        Returns
        -------
        list[EntityMention]
            Lista de entidades encontradas.
        """

        mentions: list[EntityMention] = []

        for pattern, entity_type in self._PET_PATTERNS:
            matches = re.finditer(
                pattern,
                data,
                flags=re.IGNORECASE,
            )

            for match in matches:
                mentions.append(
                    EntityMention(
                        text=match.group(1),
                        entity_type=entity_type,
                        start=match.start(1),
                        end=match.end(1),
                    )
                )

        return mentions
