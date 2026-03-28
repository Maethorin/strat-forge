"""Resolution typing contracts for StratForge."""

import typing


@typing.runtime_checkable
class ThreeDiceRollContract(typing.Protocol):
    """Describe the structural contract exposed by a three-dice roll entity."""

    first_die: int
    second_die: int
    third_die: int

    @property
    def total(self) -> int:
        """Return the total value of the three dice."""

    def is_success_against(self, target_number: int) -> bool:
        """Return whether the roll succeeds against a target number."""

    def is_critical_success_against(self, target_number: int) -> bool:
        """Return whether the roll is a critical success against a target number."""

    def is_critical_failure_against(self, target_number: int) -> bool:
        """Return whether the roll is a critical failure against a target number."""
