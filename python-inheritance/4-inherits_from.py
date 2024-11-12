#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class
that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
