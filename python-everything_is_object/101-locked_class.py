#!/usr/bin/python3
"""
This module defines the LockedClass.
"""


class LockedClass:
    """
    LockedClass restricts the creation of
    instance attributes to only 'first_name'.
    """

    __slots__ = ["first_name"]
