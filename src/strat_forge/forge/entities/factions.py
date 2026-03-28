"""Faction domain models for StratForge."""

import dataclasses
import enum
import typing

from strat_forge.forge.types import traits


class FactionDoctrine(enum.StrEnum):
    """Represent the strategic doctrine that defines an RTS faction."""

    CONVENTIONAL = "conventional"
    ELITE = "elite"
    MOBILE = "mobile"
    SIEGE = "siege"
    SWARM = "swarm"

    @classmethod
    def create(cls, value: str) -> typing.Self:
        """Create a faction doctrine from its canonical value."""
        return cls(value)


@dataclasses.dataclass(frozen=True, slots=True)
class Faction:
    """Represent a playable RTS faction described through GURPS traits."""

    name: str
    doctrine: FactionDoctrine
    advantages: tuple[traits.AdvantageContract, ...]
    disadvantages: tuple[traits.DisadvantageContract, ...]

    @classmethod
    def create(cls, name: str, doctrine: FactionDoctrine, advantages: tuple[traits.AdvantageContract, ...] = (), disadvantages: tuple[traits.DisadvantageContract, ...] = ()) -> typing.Self:
        """Create a faction from its doctrine and trait lists."""
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError("Faction name should not be blank")

        trait_names = tuple(advantage.name for advantage in advantages) + tuple(disadvantage.name for disadvantage in disadvantages)

        if len(trait_names) != len(set(trait_names)):
            raise ValueError("Faction trait names should be unique")

        return cls(name=normalized_name, doctrine=doctrine, advantages=advantages, disadvantages=disadvantages)

    @property
    def total_trait_point_cost(self) -> int:
        """Return the total point cost contributed by the faction traits."""
        return sum(advantage.point_cost for advantage in self.advantages) + sum(disadvantage.point_cost for disadvantage in self.disadvantages)

    def has_trait_named(self, trait_name: str) -> bool:
        """Return whether the faction includes a trait with the given name."""
        return trait_name in tuple(advantage.name for advantage in self.advantages) or trait_name in tuple(disadvantage.name for disadvantage in self.disadvantages)
