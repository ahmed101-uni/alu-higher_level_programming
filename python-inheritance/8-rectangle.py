#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with the specified width and
        height after validation.
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
