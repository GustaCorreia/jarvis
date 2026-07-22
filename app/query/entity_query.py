from __future__ import annotations


class EntityQuery:
    """
    Read-only access to entities stored in the WorldModel.
    """

    def __init__(self, world_model):
        self._world_model = world_model

    def by_id(self, entity_id):
        return self._world_model.get_entity(entity_id)
