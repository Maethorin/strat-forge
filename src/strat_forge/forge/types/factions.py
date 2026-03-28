"""Faction typing contracts for StratForge."""

import typing


@typing.runtime_checkable
class FactionContract(typing.Protocol):
    """Describe the structural contract exposed by a faction entity."""

    name: str
    doctrine: object
    advantages: tuple[object, ...]
    disadvantages: tuple[object, ...]

    @property
    def total_trait_point_cost(self) -> int:
        """Return the total point cost contributed by the faction traits."""

    def has_trait_named(self, trait_name: str) -> bool:
        """Return whether the faction includes a trait with the given name."""
