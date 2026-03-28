"""Unit tests for the ``strat_forge.exceptions`` module."""

from strat_forge import exceptions


class TestGettingInvalidDomainException:
    """Describe the shared invalid domain exception contract."""

    def test_should_define_invalid_domain_as_an_exception_type(self) -> None:
        """Assert that InvalidDomain remains part of the exception hierarchy."""
        assert issubclass(exceptions.InvalidDomain, Exception)

    def test_should_keep_the_exception_message_when_raised(self) -> None:
        """Assert that InvalidDomain preserves its message."""
        exception = exceptions.InvalidDomain("invalid domain configuration")

        assert str(exception) == "invalid domain configuration"
