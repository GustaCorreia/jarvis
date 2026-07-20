from app.cognition.core.mention import Mention


def test_create_mention():
    mention = Mention(
        text="Thor",
        start=14,
        end=18,
    )

    assert mention.text == "Thor"
    assert mention.start == 14
    assert mention.end == 18

    # Herdados de CognitiveObject
    assert mention.confidence == 1.0
    assert mention.source == "system"

    assert mention.metadata == {}
