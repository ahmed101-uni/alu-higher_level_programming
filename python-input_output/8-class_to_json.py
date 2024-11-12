#!/usr/bin/python3
"""
Module with `class_to_json` function for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary representation
    suitable for JSON serialization.
    """

    return obj.__dict__
