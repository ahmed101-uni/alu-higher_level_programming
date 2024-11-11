#!/usr/bin/python3
"""
This module defines a MagicClass that performs calculations for a circle.
"""
import math


class MagicClass:
    """
    MagicClass

    A class used to represent a circle with
    methods to calculate its area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius
        return None

    def area(self):
        """
        Calculate the area of the circle.
        """
        return self._MagicClass__radius**2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.
        """

        return 2 * math.pi * self._MagicClass__radius
