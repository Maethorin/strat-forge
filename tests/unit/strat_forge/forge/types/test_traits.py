"""Unit tests for the ``strat_forge.forge.types.traits`` module."""

from strat_forge.forge.entities import traits as entity_traits
from strat_forge.forge.types import traits


class TestGettingTraitTypesModuleDocumentation:
    """Describe the trait types module documentation contract."""

    def test_should_define_the_trait_types_module_docstring(self) -> None:
        """Assert that the trait types module exposes a top-level docstring."""
        assert traits.__doc__ == "Trait typing contracts for StratForge."


class TestMatchingTraitProtocols:
    """Describe the trait protocol conformance contract."""

    def test_should_match_the_advantage_protocol(self) -> None:
        """Assert that the concrete advantage entity conforms to the advantage protocol."""
        advantage = entity_traits.Advantage.create(name="Combat Reflexes", point_cost=15)

        assert isinstance(advantage, traits.AdvantageContract)

    def test_should_match_the_disadvantage_protocol(self) -> None:
        """Assert that the concrete disadvantage entity conforms to the disadvantage protocol."""
        disadvantage = entity_traits.Disadvantage.create(name="Bad Temper", point_cost=-10)

        assert isinstance(disadvantage, traits.DisadvantageContract)
