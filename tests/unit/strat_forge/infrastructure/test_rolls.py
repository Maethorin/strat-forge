"""Unit tests for the ``strat_forge.infrastructure.rolls`` module."""

import strat_forge.infrastructure.rolls as rolls


class TestRollingThreeDice:
    """Describe the three-dice infrastructure rolling contract."""

    def test_should_roll_three_dice_and_return_a_domain_roll(self, monkeypatch) -> None:
        """Assert that the roller returns a three-dice domain roll."""
        generated_values = iter((2, 4, 5))

        def fake_randint(start: int, end: int) -> int:
            assert start == 1
            assert end == 6
            return next(generated_values)

        monkeypatch.setattr(rolls, "randint", fake_randint)

        three_dice_roller = rolls.ThreeDiceRoller.create()
        three_dice_roll = three_dice_roller.roll()

        assert three_dice_roll.first_die == 2
        assert three_dice_roll.second_die == 4
        assert three_dice_roll.third_die == 5
        assert three_dice_roll.total == 11
