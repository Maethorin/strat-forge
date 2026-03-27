"""Unit tests for the ``strat_forge`` package module."""

from strat_forge import __version__


class TestGettingPackageVersion:
    """Describe the package version contract."""

    def test_should_expose_the_package_version(self) -> None:
        """Assert that the package version is defined."""
        assert __version__ == "0.0.1"
