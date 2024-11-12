#!/usr/bin/python3
"""
This module provides a function to check if an object
is an instance of, or if the object is an instance of
a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class.
    """
    return issubclass(type(obj), a_class)
