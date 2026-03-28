"""Infrastructure dice generators for StratForge."""

import random
import typing


class ThreeDiceRoller(object):
    """Generate three-dice rolls using the standard random module."""

    @classmethod
    def create(cls) -> typing.Self:
        """Create a three-dice roller."""
        return cls()

    def roll(self) -> tuple[int, int, int]:
        """Roll three six-sided dice and return the generated die values."""
        return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
