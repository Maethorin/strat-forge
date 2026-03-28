"""Trait typing contracts for StratForge."""

import typing


@typing.runtime_checkable
class AdvantageContract(typing.Protocol):
    """Describe the structural contract exposed by an advantage entity."""

    name: str
    point_cost: int


@typing.runtime_checkable
class DisadvantageContract(typing.Protocol):
    """Describe the structural contract exposed by a disadvantage entity."""

    name: str
    point_cost: int
