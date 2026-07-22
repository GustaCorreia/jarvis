from app.core import CognitiveCore


class FakeResult:
    pass


class FakeOperation:
    pass


class FakeEntity:
    pass


class FakeWorldModel:
    pass


class FakeMemoryEngine:

    def __init__(self):
        self.called = False
        self.operation = None
        self.world = None

    def apply(self, operation, world_model):
        self.called = True
        self.operation = operation
        self.world = world_model
        return FakeResult()


class FakeReasoningEngine:

    def entity_by_id(self, entity_id):
        return entity_id


class FakeKnowledgeBuilder:

    def build_add_entity(self, entity):
        return FakeOperation()


def test_core_learn_delegates_to_memory():
    world = FakeWorldModel()
    memory = FakeMemoryEngine()

    core = CognitiveCore(
        world_model=world,
        memory=memory,
        reasoning=FakeReasoningEngine(),
        builder=FakeKnowledgeBuilder(),
    )

    result = core.learn("operation")

    assert memory.called
    assert memory.world is world
    assert isinstance(result, FakeResult)


def test_core_learn_entity_uses_builder():
    world = FakeWorldModel()
    memory = FakeMemoryEngine()

    core = CognitiveCore(
        world_model=world,
        memory=memory,
        reasoning=FakeReasoningEngine(),
        builder=FakeKnowledgeBuilder(),
    )

    result = core.learn_entity(FakeEntity())

    assert memory.called
    assert isinstance(memory.operation, FakeOperation)
    assert isinstance(result, FakeResult)


def test_core_ask_entity():
    core = CognitiveCore(
        world_model=FakeWorldModel(),
        memory=FakeMemoryEngine(),
        reasoning=FakeReasoningEngine(),
        builder=FakeKnowledgeBuilder(),
    )

    assert core.ask_entity("abc") == "abc"
