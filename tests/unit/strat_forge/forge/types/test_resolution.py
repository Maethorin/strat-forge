"""Unit tests for the ``strat_forge.forge.types.resolution`` module."""

from strat_forge.forge.resolution import rolls
from strat_forge.forge.types import resolution


class TestGettingResolutionTypesModuleDocumentation:
    """Describe the resolution types module documentation contract."""

    def test_should_define_the_resolution_types_module_docstring(self) -> None:
        """Assert that the resolution types module exposes a top-level docstring."""
        assert resolution.__doc__ == "Resolution typing contracts for StratForge."


class TestMatchingResolutionProtocols:
    """Describe the resolution protocol conformance contract."""

    def test_should_match_the_three_dice_roll_protocol(self) -> None:
        """Assert that the concrete three-dice roll entity conforms to the resolution protocol."""
        three_dice_roll = rolls.ThreeDiceRoll.create(2, 4, 5)

        assert isinstance(three_dice_roll, resolution.ThreeDiceRollContract)
