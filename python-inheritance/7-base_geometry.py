#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    This module defines a BaseGeometry class.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer and greater than 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
