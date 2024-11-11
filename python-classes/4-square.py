#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    A class used to represent a Square.
    """

    def __init__(self, size=0):
        """
        Initialize the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Property that retrieves the size of the square (getter).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size**2
