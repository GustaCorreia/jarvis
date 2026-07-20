from app.cognition.entities.entity_mention import EntityMention
from app.cognition.entities.entity_type import EntityType


def test_create_entity_mention():
    mention = EntityMention(
        text="Thor",
        entity_type=EntityType.PET,
        start=14,
        end=18,
    )

    assert mention.text == "Thor"
    assert mention.entity_type == EntityType.PET
    assert mention.start == 14
    assert mention.end == 18
