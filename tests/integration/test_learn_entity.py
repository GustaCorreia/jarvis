from app.core import CognitiveCore
from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.world_model import WorldModel
from app.knowledge import KnowledgeBuilder
from app.memory.engine import MemoryEngine
from app.memory.handler_registry import HandlerRegistry
from app.memory.handlers.add_entity_handler import AddEntityHandler
from app.reasoning import ReasoningEngine


def test_core_can_learn_real_entity():

    world = WorldModel()

    registry = HandlerRegistry()
    registry.register(AddEntityHandler())

    memory = MemoryEngine(registry)

    reasoning = ReasoningEngine(world)

    builder = KnowledgeBuilder()

    core = CognitiveCore(
        world_model=world,
        memory=memory,
        reasoning=reasoning,
        builder=builder,
    )

    entity = Entity(
        entity_type=EntityType.UNKNOWN,
    )

    result = core.learn_entity(entity)

    assert result.success

    learned = core.ask_entity(entity.id)

    assert learned is entity

    assert world.entity_count == 1
