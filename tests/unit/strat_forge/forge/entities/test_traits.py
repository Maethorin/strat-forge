"""Unit tests for the ``strat_forge.forge.entities.traits`` module."""

import pytest

from strat_forge.forge.entities import traits


class TestGettingTraitsModuleDocumentation:
    """Describe the traits module documentation contract."""

    def test_should_define_the_traits_module_docstring(self) -> None:
        """Assert that the traits module exposes a top-level docstring."""
        assert traits.__doc__ == "Trait domain models for StratForge."


class TestCreatingAdvantage:
    """Describe the advantage creation contract."""

    def test_should_create_an_advantage_from_domain_values(self) -> None:
        """Assert that an advantage keeps the configured domain values."""
        advantage = traits.Advantage.create(name="Combat Reflexes", point_cost=15)

        assert advantage.name == "Combat Reflexes"
        assert advantage.point_cost == 15

    def test_should_reject_an_advantage_with_a_non_positive_point_cost(self) -> None:
        """Assert that an advantage must have a strictly positive point cost."""
        with pytest.raises(ValueError, match="Advantage point cost should be positive"):
            traits.Advantage.create(name="Combat Reflexes", point_cost=0)


class TestCreatingDisadvantage:
    """Describe the disadvantage creation contract."""

    def test_should_create_a_disadvantage_from_domain_values(self) -> None:
        """Assert that a disadvantage keeps the configured domain values."""
        disadvantage = traits.Disadvantage.create(name="Bad Temper", point_cost=-10)

        assert disadvantage.name == "Bad Temper"
        assert disadvantage.point_cost == -10

    def test_should_reject_a_disadvantage_with_a_non_negative_point_cost(self) -> None:
        """Assert that a disadvantage must have a strictly negative point cost."""
        with pytest.raises(ValueError, match="Disadvantage point cost should be negative"):
            traits.Disadvantage.create(name="Bad Temper", point_cost=0)
