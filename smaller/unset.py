from .sentinel import Sentinel


"""
Sentinel for identifying omitted parameter vs parameter explicitly set to None etc.

Usage:
    def func(param=UNSET):
        if param is UNSET:
            ...
"""
UNSET = Sentinel(name="UNSET", truthy=False)
