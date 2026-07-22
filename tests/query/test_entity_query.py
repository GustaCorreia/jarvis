from app.query import EntityQuery


class FakeWorldModel:

    def __init__(self):
        self.entity = object()

    def get_entity(self, entity_id):
        return self.entity


def test_entity_query_returns_entity():
    world = FakeWorldModel()

    query = EntityQuery(world)

    assert query.by_id("123") is world.entity
