"""Unit tests for the ``strat_forge.forge.entities.factions`` module."""

import pytest

from strat_forge.forge.entities import factions, traits


class TestGettingFactionsModuleDocumentation:
    """Describe the factions module documentation contract."""

    def test_should_define_the_factions_module_docstring(self) -> None:
        """Assert that the factions module exposes a top-level docstring."""
        assert factions.__doc__ == "Faction domain models for StratForge."


class TestCreatingFactionDoctrine:
    """Describe the faction doctrine creation contract."""

    def test_should_define_the_mobile_doctrine_code(self) -> None:
        """Assert that the mobile doctrine keeps its canonical value."""
        assert factions.FactionDoctrine.MOBILE.value == "mobile"


class TestCreatingFaction:
    """Describe the faction creation contract."""

    def test_should_create_a_faction_from_domain_values(self) -> None:
        """Assert that a faction keeps the configured doctrine and trait lists."""
        combat_reflexes = traits.Advantage.create(name="Combat Reflexes", point_cost=15)
        fit = traits.Advantage.create(name="Fit", point_cost=5)
        bad_temper = traits.Disadvantage.create(name="Bad Temper", point_cost=-10)

        faction = factions.Faction.create(name="Iron Wolves", doctrine=factions.FactionDoctrine.MOBILE, advantages=(combat_reflexes, fit), disadvantages=(bad_temper,))

        assert faction.name == "Iron Wolves"
        assert faction.doctrine is factions.FactionDoctrine.MOBILE
        assert faction.advantages == (combat_reflexes, fit)
        assert faction.disadvantages == (bad_temper,)

    def test_should_calculate_the_total_trait_point_cost(self) -> None:
        """Assert that a faction exposes the sum of its trait point costs."""
        combat_reflexes = traits.Advantage.create(name="Combat Reflexes", point_cost=15)
        fit = traits.Advantage.create(name="Fit", point_cost=5)
        bad_temper = traits.Disadvantage.create(name="Bad Temper", point_cost=-10)

        faction = factions.Faction.create(name="Iron Wolves", doctrine=factions.FactionDoctrine.MOBILE, advantages=(combat_reflexes, fit), disadvantages=(bad_temper,))

        assert faction.total_trait_point_cost == 10

    def test_should_report_whether_the_faction_has_a_named_trait(self) -> None:
        """Assert that a faction can resolve its traits by name."""
        combat_reflexes = traits.Advantage.create(name="Combat Reflexes", point_cost=15)
        bad_temper = traits.Disadvantage.create(name="Bad Temper", point_cost=-10)

        faction = factions.Faction.create(name="Iron Wolves", doctrine=factions.FactionDoctrine.MOBILE, advantages=(combat_reflexes,), disadvantages=(bad_temper,))

        assert faction.has_trait_named("Combat Reflexes") is True
        assert faction.has_trait_named("Bad Temper") is True
        assert faction.has_trait_named("Fit") is False

    def test_should_reject_a_faction_with_a_blank_name(self) -> None:
        """Assert that a faction must have a non-blank name."""
        with pytest.raises(ValueError, match="Faction name should not be blank"):
            factions.Faction.create(name="   ", doctrine=factions.FactionDoctrine.MOBILE)

    def test_should_reject_a_faction_with_duplicate_trait_names(self) -> None:
        """Assert that a faction cannot contain duplicate trait names."""
        combat_reflexes = traits.Advantage.create(name="Combat Reflexes", point_cost=15)
        duplicated_combat_reflexes = traits.Advantage.create(name="Combat Reflexes", point_cost=15)

        with pytest.raises(ValueError, match="Faction trait names should be unique"):
            factions.Faction.create(name="Iron Wolves", doctrine=factions.FactionDoctrine.MOBILE, advantages=(combat_reflexes, duplicated_combat_reflexes))
