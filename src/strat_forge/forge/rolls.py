"""Roll domain models for StratForge."""

from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, slots=True)
class ThreeDiceRoll:
    """Represent a roll composed of three six-sided dice."""

    first_die: int
    second_die: int
    third_die: int

    @classmethod
    def create(cls, first_die: int, second_die: int, third_die: int) -> Self:
        """Create a three-dice roll from individual die values."""
        return cls(first_die=first_die, second_die=second_die, third_die=third_die)

    @property
    def total(self) -> int:
        """Return the total value of the three dice."""
        return self.first_die + self.second_die + self.third_die

    def is_success_against(self, target_number: int) -> bool:
        """Return whether the roll succeeds against a GURPS target number."""
        if self.is_critical_success_against(target_number):
            return True

        if self.total in (17, 18):
            return False

        return self.total <= target_number

    def is_critical_success_against(self, target_number: int) -> bool:
        """Return whether the roll is a critical success against the target."""
        return self.total in (3, 4) or (self.total == 5 and target_number >= 15) or (self.total == 6 and target_number >= 16)

    def is_critical_failure_against(self, target_number: int) -> bool:
        """Return whether the roll is a critical failure against the target."""
        return self.total == 18 or (self.total == 17 and target_number <= 15) or self.total - target_number >= 10
