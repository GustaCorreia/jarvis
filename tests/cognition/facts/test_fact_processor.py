from app.cognition.entities.entity_mention import EntityMention
from app.cognition.entities.entity_type import EntityType
from app.cognition.facts.fact_processor import FactProcessor
from app.cognition.facts.fact_type import FactType
from app.cognition.understanding.understanding import Understanding


def test_empty_understanding_returns_empty_fact_list():
    processor = FactProcessor()

    understanding = Understanding(
        text=""
    )

    facts = processor.process(understanding)

    assert facts == []


def test_entity_generates_fact():
    processor = FactProcessor()

    understanding = Understanding(
        text="Thor",
        confidence=1.0,
        entities=[
            EntityMention(
                text="Thor",
                start=0,
                end=4,
                entity_type=EntityType.PET,
            )
        ],
    )

    facts = processor.process(understanding)

    assert len(facts) == 1

    fact = facts[0]

    assert fact.subject == "message"
    assert fact.predicate == "mentions"
    assert fact.value == "Thor"
    assert fact.fact_type == FactType.ATTRIBUTE
    assert fact.confidence == 1.0
