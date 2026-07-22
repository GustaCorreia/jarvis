from app.memory.confidence import ConfidencePolicy


def test_accepts_confidence_above_threshold():
    policy = ConfidencePolicy()

    assert policy.accepts(0.80)


def test_rejects_confidence_below_threshold():
    policy = ConfidencePolicy()

    assert not policy.accepts(0.30)


def test_accepts_exact_threshold():
    policy = ConfidencePolicy(minimum_confidence=0.70)

    assert policy.accepts(0.70)
