from app.domain.entity import Entity


class EntityResolver:
    """
    Localiza uma entidade existente utilizando
    mentions ou aliases armazenados nos Facts.
    """

    def __init__(self, world):
        self._world = world

    def _normalize(self, value: str) -> str:
        """
        Normaliza uma mention para comparação.
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
                    fact.attribute in ("mention", "alias")
                    and self._normalize(fact.value) == mention
                ):
                    return entity

        return None
