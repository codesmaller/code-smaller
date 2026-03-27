
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Sentinel:
    """
    Custom truthy or falsy "sentinel" object for representing special states or values.

    Usage:
        DEFAULT = Sentinel(name="DEFAULT", truthy=True)

        if value is DEFAULT:
            ...
    """

    # object representation string for logs and debugging
    name: str

    # whether the sentinel should evaluate to True or False in if statements
    truthy: bool

    def __bool__(self) -> bool:
        return self.truthy

    def __repr__(self) -> str:
        return f"{self.name}"
