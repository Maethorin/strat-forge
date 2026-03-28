"""Trait domain models for StratForge."""

import dataclasses
import typing


@dataclasses.dataclass(frozen=True, slots=True)
class Advantage:
    """Represent a GURPS advantage with a positive point cost."""

    name: str
    point_cost: int

    @classmethod
    def create(cls, name: str, point_cost: int) -> typing.Self:
        """Create an advantage from its domain values."""
        if point_cost <= 0:
            raise ValueError("Advantage point cost should be positive")

        return cls(name=name, point_cost=point_cost)


@dataclasses.dataclass(frozen=True, slots=True)
class Disadvantage:
    """Represent a GURPS disadvantage with a negative point cost."""

    name: str
    point_cost: int

    @classmethod
    def create(cls, name: str, point_cost: int) -> typing.Self:
        """Create a disadvantage from its domain values."""
        if point_cost >= 0:
            raise ValueError("Disadvantage point cost should be negative")

        return cls(name=name, point_cost=point_cost)
