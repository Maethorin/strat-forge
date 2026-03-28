"""strat_forge package."""

__all__ = ["__version__"]

__version__ = "0.0.1"


class ClassProperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


classproperty = ClassProperty
