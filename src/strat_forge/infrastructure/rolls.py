"""Infrastructure roll generators for StratForge."""

import random
import typing

from strat_forge import services


class ThreeDiceRoller(object):
    """Generate three-dice rolls using the standard random module."""

    @classmethod
    def create(cls) -> typing.Self:
        """Create a three-dice roller."""
        return cls()

    def roll(self) -> object:
        """Roll three six-sided dice and return the domain roll object."""
        return services.RollService.domain.ThreeDiceRoll.create(first_die=random.randint(1, 6), second_die=random.randint(1, 6), third_die=random.randint(1, 6))
