from app.cognition.knowledge.knowledge_pipeline import KnowledgePipeline


class FakeBuilder:
    def __init__(self):
        self.called = False

    def build(self, facts):
        self.called = True
        assert facts == ["fact"]
        return "operations"


class FakePlanner:
    def __init__(self):
        self.called = False

    def build(self, operations):
        self.called = True
        assert operations == "operations"
        return "plan"


class FakeExecutor:
    def __init__(self):
        self.called = False

    def execute(self, plan):
        self.called = True
        assert plan == "plan"
        return "result"


def test_pipeline_executes_complete_learning_flow():
    builder = FakeBuilder()
    planner = FakePlanner()
    executor = FakeExecutor()

    pipeline = KnowledgePipeline(
        builder=builder,
        planner=planner,
        executor=executor,
    )

    result = pipeline.learn(["fact"])

    assert builder.called
    assert planner.called
    assert executor.called

    assert result == "result"
