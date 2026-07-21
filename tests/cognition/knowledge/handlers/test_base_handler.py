import pytest

from app.cognition.knowledge.handlers.base_handler import (
    BaseKnowledgeHandler,
)


def test_base_handler_is_abstract():
    with pytest.raises(TypeError):
        BaseKnowledgeHandler()
