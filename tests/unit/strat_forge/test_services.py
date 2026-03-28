"""Unit tests for the ``strat_forge.services`` module."""

import importlib

import pytest

from strat_forge import exceptions, services


class SkillService(services.Service):
    """Concrete service used to validate import-based domain resolution."""

    _domain = "strat_forge.forge.skills"


class TestGettingServiceDomain:
    """Describe the service domain resolution contract."""

    def test_should_raise_invalid_domain_for_the_base_service(self) -> None:
        """Assert that the abstract service cannot resolve a domain by default."""
        with pytest.raises(exceptions.InvalidDomain, match="You should use a specific service implementation"):
            services.Service.domain

    def test_should_import_the_configured_domain_module_for_a_specific_service(self) -> None:
        """Assert that a concrete service resolves its configured module path."""
        expected_module = importlib.import_module("strat_forge.forge.skills")

        assert SkillService.domain is expected_module

    def test_should_import_the_roll_domain_module_for_the_roll_service(self) -> None:
        """Assert that the roll service resolves the roll domain module."""
        expected_module = importlib.import_module("strat_forge.forge.rolls")

        assert services.RollService.domain is expected_module
