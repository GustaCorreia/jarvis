from app.cognition.knowledge.executor import KnowledgeExecutor
from app.cognition.knowledge.knowledge_builder import KnowledgeBuilder
from app.cognition.knowledge.knowledge_planner import KnowledgePlanner


class KnowledgePipeline:
    """
    Orquestra o pipeline de conhecimento.

    Fluxo:

        Facts
          │
          ▼
    KnowledgeBuilder
          │
          ▼
    KnowledgePlanner
          │
          ▼
    KnowledgeExecutor

    Esta classe NÃO implementa regras de negócio.
    Sua única responsabilidade é coordenar os componentes.
    """

    def __init__(
        self,
        builder: KnowledgeBuilder,
        planner: KnowledgePlanner,
        executor: KnowledgeExecutor,
    ):
        self._builder = builder
        self._planner = planner
        self._executor = executor

    def learn(self, facts):
        operations = self._builder.build(facts)

        plan = self._planner.build(operations)

        return self._executor.execute(plan)
