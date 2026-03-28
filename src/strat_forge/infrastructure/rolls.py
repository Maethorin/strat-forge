"""Infrastructure roll generators for StratForge."""

from random import randint
from typing import Self

from strat_forge.services import RollService


class ThreeDiceRoller(object):
    """Generate three-dice rolls using the standard random module."""

    @classmethod
    def create(cls) -> Self:
        """Create a three-dice roller."""
        return cls()

    def roll(self) -> object:
        """Roll three six-sided dice and return the domain roll object."""
        return RollService.domain.ThreeDiceRoll.create(first_die=randint(1, 6), second_die=randint(1, 6), third_die=randint(1, 6))
