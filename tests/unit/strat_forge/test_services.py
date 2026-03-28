"""Unit tests for the ``strat_forge.services`` module."""

import importlib

import pytest

from strat_forge import exceptions, services


class SkillService(services.Service):
    """Concrete service used to validate import-based domain resolution."""

    _domain = "strat_forge.forge.skills"

    @classmethod
    def get_a_skill_module(cls) -> object:
        """Return the configured skill domain module."""
        return cls.domain


class UnconfiguredService(services.Service):
    """Concrete service without a configured domain used for validation."""

    @classmethod
    def get_a_domain_module(cls) -> object:
        """Return the configured domain module."""
        return cls.domain


class TestGettingServiceDomain:
    """Describe the service domain resolution contract."""

    def test_should_raise_invalid_domain_for_a_service_without_a_concrete_domain(self) -> None:
        """Assert that a service without a configured domain cannot resolve a module."""
        with pytest.raises(exceptions.InvalidDomain, match="You should use a specific service implementation"):
            UnconfiguredService.get_a_domain_module()

    def test_should_return_the_configured_domain_module_through_a_service_method(self) -> None:
        """Assert that a concrete service resolves its configured module through a public method."""
        expected_module = importlib.import_module("strat_forge.forge.skills")

        assert SkillService.get_a_skill_module() is expected_module

    def test_should_create_a_three_dice_roll_through_a_service_factory_method(self) -> None:
        """Assert that the roll service exposes an explicit factory method for domain object creation."""
        three_dice_roll = services.RollService.create_a_three_dice_roll(2, 4, 5)

        assert three_dice_roll.first_die == 2
        assert three_dice_roll.second_die == 4
        assert three_dice_roll.third_die == 5
        assert three_dice_roll.total == 11
