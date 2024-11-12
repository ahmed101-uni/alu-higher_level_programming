#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    This module defines a BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with the specified width and
        height after validation.
        """
        self.__height = height
        self.__width = width

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string is formatted as "width/height".
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer and greater than 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(width, height)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


class Square(BaseGeometry):
    """
    A class used to represent a Square, which
    inherits from BaseGeometry.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
