from app.reasoning import ReasoningEngine


class FakeKnowledge:
    pass


class FakeWorldModel:

    def __init__(self):
        self.knowledge = FakeKnowledge()

    def get_knowledge(self, entity_id):
        return self.knowledge


def test_reasoning_returns_knowledge():
    world = FakeWorldModel()

    engine = ReasoningEngine(world)

    knowledge = engine.knowledge_for("entity")

    assert knowledge is world.knowledge
