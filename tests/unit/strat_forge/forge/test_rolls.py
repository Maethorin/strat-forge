"""Unit tests for the ``strat_forge.forge.rolls`` module."""

import strat_forge.forge.rolls as rolls


class TestCreatingThreeDiceRoll:
    """Describe the three-dice roll creation contract."""

    def test_should_create_a_three_dice_roll_from_three_die_values(self) -> None:
        """Assert that the roll keeps the configured die values."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 3, 6)

        assert three_dice_roll.first_die == 1
        assert three_dice_roll.second_die == 3
        assert three_dice_roll.third_die == 6

    def test_should_calculate_the_total_of_the_three_dice(self) -> None:
        """Assert that the roll exposes the sum of its three dice."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 3, 6)

        assert three_dice_roll.total == 10


class TestResolvingSuccessAgainstATargetNumber:
    """Describe the standard GURPS success resolution contract."""

    def test_should_succeed_when_the_total_is_not_greater_than_the_target_number(self) -> None:
        """Assert that a roll succeeds when it does not exceed the target."""
        three_dice_roll = rolls.ThreeDiceRoll.create(3, 4, 5)

        assert three_dice_roll.is_success_against(12) is True

    def test_should_fail_when_the_total_is_greater_than_the_target_number(self) -> None:
        """Assert that a roll fails when it exceeds the target."""
        three_dice_roll = rolls.ThreeDiceRoll.create(4, 4, 5)

        assert three_dice_roll.is_success_against(12) is False

    def test_should_fail_on_a_roll_of_seventeen_even_with_a_higher_target_number(self) -> None:
        """Assert that a roll of seventeen is always a failure."""
        three_dice_roll = rolls.ThreeDiceRoll.create(6, 5, 6)

        assert three_dice_roll.is_success_against(18) is False

    def test_should_fail_on_a_roll_of_eighteen_even_with_a_higher_target_number(self) -> None:
        """Assert that a roll of eighteen is always a failure."""
        three_dice_roll = rolls.ThreeDiceRoll.create(6, 6, 6)

        assert three_dice_roll.is_success_against(18) is False


class TestResolvingCriticalSuccessAgainstATargetNumber:
    """Describe the GURPS critical success resolution contract."""

    def test_should_critically_succeed_on_a_roll_of_three(self) -> None:
        """Assert that a roll of three is always a critical success."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 1, 1)

        assert three_dice_roll.is_critical_success_against(10) is True

    def test_should_critically_succeed_on_a_roll_of_four(self) -> None:
        """Assert that a roll of four is always a critical success."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 1, 2)

        assert three_dice_roll.is_critical_success_against(10) is True

    def test_should_critically_succeed_on_a_roll_of_five_with_target_fifteen(self) -> None:
        """Assert that a roll of five is critical at target fifteen or higher."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 2, 2)

        assert three_dice_roll.is_critical_success_against(15) is True

    def test_should_not_critically_succeed_on_a_roll_of_five_below_target_fifteen(self) -> None:
        """Assert that a roll of five is not critical below target fifteen."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 2, 2)

        assert three_dice_roll.is_critical_success_against(14) is False

    def test_should_critically_succeed_on_a_roll_of_six_with_target_sixteen(self) -> None:
        """Assert that a roll of six is critical at target sixteen or higher."""
        three_dice_roll = rolls.ThreeDiceRoll.create(1, 2, 3)

        assert three_dice_roll.is_critical_success_against(16) is True


class TestResolvingCriticalFailureAgainstATargetNumber:
    """Describe the GURPS critical failure resolution contract."""

    def test_should_critically_fail_on_a_roll_of_eighteen(self) -> None:
        """Assert that a roll of eighteen is always a critical failure."""
        three_dice_roll = rolls.ThreeDiceRoll.create(6, 6, 6)

        assert three_dice_roll.is_critical_failure_against(16) is True

    def test_should_critically_fail_on_a_roll_of_seventeen_with_target_fifteen(self) -> None:
        """Assert that a roll of seventeen is critical at target fifteen or lower."""
        three_dice_roll = rolls.ThreeDiceRoll.create(6, 5, 6)

        assert three_dice_roll.is_critical_failure_against(15) is True

    def test_should_not_critically_fail_on_a_roll_of_seventeen_with_target_sixteen(self) -> None:
        """Assert that a roll of seventeen is not critical at target sixteen or higher."""
        three_dice_roll = rolls.ThreeDiceRoll.create(6, 5, 6)

        assert three_dice_roll.is_critical_failure_against(16) is False

    def test_should_critically_fail_when_the_roll_is_ten_greater_than_the_target_number(self) -> None:
        """Assert that a roll ten above the target is a critical failure."""
        three_dice_roll = rolls.ThreeDiceRoll.create(5, 5, 6)

        assert three_dice_roll.is_critical_failure_against(6) is True
