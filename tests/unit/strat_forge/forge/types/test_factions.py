"""Unit tests for the ``strat_forge.forge.types.factions`` module."""

from strat_forge.forge.entities import factions as entity_factions, traits as entity_traits
from strat_forge.forge.types import factions


class TestGettingFactionTypesModuleDocumentation:
    """Describe the faction types module documentation contract."""

    def test_should_define_the_faction_types_module_docstring(self) -> None:
        """Assert that the faction types module exposes a top-level docstring."""
        assert factions.__doc__ == "Faction typing contracts for StratForge."


class TestMatchingFactionProtocols:
    """Describe the faction protocol conformance contract."""

    def test_should_match_the_faction_protocol(self) -> None:
        """Assert that the concrete faction entity conforms to the faction protocol."""
        combat_reflexes = entity_traits.Advantage.create(name="Combat Reflexes", point_cost=15)
        bad_temper = entity_traits.Disadvantage.create(name="Bad Temper", point_cost=-10)
        faction = entity_factions.Faction.create(name="Iron Wolves", doctrine=entity_factions.FactionDoctrine.MOBILE, advantages=(combat_reflexes,), disadvantages=(bad_temper,))

        assert isinstance(faction, factions.FactionContract)
