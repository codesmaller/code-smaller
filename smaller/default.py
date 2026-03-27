from .sentinel import Sentinel


"""
Sentinel placeholder for default values.

Usage:
    def func(param=DEFAULT):
        if param is DEFAULT:
            ...
"""
DEFAULT = Sentinel(name="DEFAULT", truthy=True)
