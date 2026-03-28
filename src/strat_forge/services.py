"""Service layer primitives for StratForge."""

from importlib import import_module
from types import ModuleType
from typing import Self

from strat_forge import classproperty, exceptions


class Service(object):
    """Base service that resolves a configured project module lazily."""

    _domain: str | None = None

    @classmethod
    def create(cls) -> Self:
        """Create a service instance."""
        return cls()

    @classproperty
    def domain(cls) -> ModuleType:
        """Return the configured domain module for the concrete service."""
        if cls._domain is None:
            raise exceptions.InvalidDomain("You should use a specific service implementation")
        return import_module(cls._domain)


class RollService(Service):
    """Resolve the roll domain module."""

    _domain = "strat_forge.forge.rolls"
