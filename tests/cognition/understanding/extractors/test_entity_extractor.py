from app.cognition.entities.entity_type import EntityType
from app.cognition.understanding.extractors.entity_extractor import (
    EntityExtractor,
)


def test_extract_pet():
    extractor = EntityExtractor()

    entities = extractor.process(
        "Meu cachorro Thor tomou vacina."
    )

    assert len(entities) == 1
    assert entities[0].text == "Thor"
    assert entities[0].entity_type == EntityType.PET


def test_extract_cat():
    extractor = EntityExtractor()

    entities = extractor.process(
        "Minha gata Mia está dormindo."
    )

    assert len(entities) == 1
    assert entities[0].text == "Mia"
    assert entities[0].entity_type == EntityType.PET


def test_no_context_returns_empty():
    extractor = EntityExtractor()

    entities = extractor.process(
        "Thor tomou vacina."
    )

    assert entities == []
