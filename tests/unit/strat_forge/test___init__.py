"""Unit tests for the ``strat_forge`` package module."""

import strat_forge


class TestGettingPackageVersion:
    """Describe the package version contract."""

    def test_should_expose_the_package_version(self) -> None:
        """Assert that the package version is defined."""
        assert strat_forge.__version__ == "0.0.1"

    def test_should_export_the_version_in_the_public_api(self) -> None:
        """Assert that the package public API exposes the version symbol."""
        assert "__version__" in strat_forge.__all__

    def test_should_keep_the_public_api_limited_to_the_version_symbol(self) -> None:
        """Assert that the package public API remains explicit."""
        assert strat_forge.__all__ == ["__version__"]


class TestGettingPackageDocumentation:
    """Describe the package module documentation contract."""

    def test_should_define_the_package_docstring(self) -> None:
        """Assert that the package module exposes its top-level docstring."""
        assert strat_forge.__doc__ == "strat_forge package."
