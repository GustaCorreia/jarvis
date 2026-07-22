from app.core import CognitiveCore


class FakeWorldModel:
    pass


class FakeMemoryEngine:
    pass


class FakeReasoningEngine:
    pass


class FakeKnowledgeBuilder:
    pass


def test_cognitive_core_exposes_components():
    world = FakeWorldModel()
    memory = FakeMemoryEngine()
    reasoning = FakeReasoningEngine()
    builder = FakeKnowledgeBuilder()

    core = CognitiveCore(
        world_model=world,
        memory=memory,
        reasoning=reasoning,
        builder=builder,
    )

    assert core.world_model is world
    assert core.memory is memory
    assert core.reasoning is reasoning
    assert core.builder is builder
