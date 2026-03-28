"""Custom exceptions exposed by the StratForge library."""


class InvalidDomain(Exception):
    """Raise when a service is used without a concrete domain module."""
