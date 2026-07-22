from app.domain.entity import Entity


class EntityResolver:
    """
    Localiza uma entidade existente utilizando
    a mention armazenada nos Facts.
    """

    def __init__(self, world):
        self._world = world

    def _normalize(self, value: str) -> str:
        """
        Normaliza uma mention para comparação.

        Primeira versão:
        - remove espaços extras
        - converte para minúsculas
        """
        return value.strip().lower()

    def resolve(self, operation):

        mention = operation.payload.get("mention")

        if mention is None:
            return None

        mention = self._normalize(mention)

        for entity in self._world.entities:

            facts = self._world.find_facts(entity.id)

            for fact in facts:

                if (
                    fact.attribute == "mention"
                    and self._normalize(fact.value) == mention
                ):
                    return entity

        return None
