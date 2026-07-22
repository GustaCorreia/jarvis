from __future__ import annotations

from app.domain.operations.add_entity_operation import AddEntityOperation


class KnowledgeBuilder:
    """
    Creates domain operations from structured knowledge.

    Future versions will receive data from the Understanding layer
    (LLM, NLP, voice, etc.).
    """

    def build_add_entity(self, entity):
        """
        Creates an AddEntityOperation for the given entity.
        """

        return AddEntityOperation(entity)
