"""Unit tests for the ``strat_forge.infrastructure.dices`` module."""

from strat_forge.infrastructure import dices


class TestRollingThreeDice:
    """Describe the three-dice infrastructure rolling contract."""

    def test_should_roll_three_dice_and_return_three_die_values(self, monkeypatch) -> None:
        """Assert that the roller returns three technical die values."""
        generated_values = iter((2, 4, 5))

        def fake_randint(start: int, end: int) -> int:
            assert start == 1
            assert end == 6
            return next(generated_values)

        monkeypatch.setattr(dices.random, "randint", fake_randint)

        three_dice_roller = dices.ThreeDiceRoller.create()
        three_dice_values = three_dice_roller.roll()

        assert three_dice_values == (2, 4, 5)
