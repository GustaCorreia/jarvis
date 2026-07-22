from app.reasoning import ReasoningEngine


class FakeWorldModel:
    pass


def test_reasoning_engine_keeps_world_model():
    world = FakeWorldModel()

    engine = ReasoningEngine(world)

    assert engine.world_model is world
