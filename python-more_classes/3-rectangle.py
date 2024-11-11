#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"

        return rect

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
