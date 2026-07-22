from __future__ import annotations

from app.domain.entity import Entity


class EntityResolver:
    """
    Resolve se uma entidade já existe no WorldModel.

    Nesta primeira versão, procura por um Fact
    com attribute == "mention" e value igual ao
    mention recebido na operação.
    """

    def __init__(self, world_model):
        self._world = world_model

    def resolve(self, operation) -> Entity | None:

        mention = operation.payload.get("mention")

        if mention is None:
            return None

        for entity in self._world.entities:

            facts = self._world.find_facts(entity.id)

            for fact in facts:

                if (
                    fact.attribute == "mention"
                    and fact.value == mention
                ):
                    return entity

        return None
