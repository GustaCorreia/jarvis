from app.reasoning import ReasoningEngine


class FakeWorldModel:

    def __init__(self):
        self.entity = object()

    def get_entity(self, entity_id):
        return self.entity


def test_reasoning_returns_entity():
    world = FakeWorldModel()

    engine = ReasoningEngine(world)

    entity = engine.entity_by_id("123")

    assert entity is world.entity
