from app.domain.knowledge.evidence import Evidence


def test_create_evidence():
    evidence = Evidence(
        source="user",
        content="Bob nasceu em 2019."
    )

    assert evidence.source == "user"
    assert evidence.content == "Bob nasceu em 2019."
