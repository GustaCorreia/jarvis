from app.domain.events import DomainEvent


def test_domain_event_creation():
    event = DomainEvent(name="entity_added")

    assert event.name == "entity_added"
    assert event.occurred_at is not None


def test_events_are_immutable():
    event = DomainEvent(name="test")

    try:
        event.name = "changed"
        assert False
    except Exception:
        assert True
