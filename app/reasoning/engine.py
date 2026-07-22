from __future__ import annotations


class ReasoningEngine:
    """
    Provides read-only reasoning over the WorldModel.
    """

    def __init__(self, world_model):
        self._world_model = world_model

    @property
    def world_model(self):
        return self._world_model

    def entity_by_id(self, entity_id):
        """
        Returns an entity from the WorldModel.
        """
        return self._world_model.get_entity(entity_id)

    def knowledge_for(self, entity_id):
        """
        Returns the Knowledge associated with an entity.

        If the WorldModel does not expose knowledge retrieval yet,
        None is returned.
        """

        getter = getattr(self._world_model, "get_knowledge", None)

        if getter is None:
            return None

        return getter(entity_id)
