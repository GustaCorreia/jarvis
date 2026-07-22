from app.domain.exceptions import DomainError


def test_domain_error_is_exception():
    assert issubclass(DomainError, Exception)
