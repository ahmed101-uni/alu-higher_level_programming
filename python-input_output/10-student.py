#!/usr/bin/python3
"""
Defines a `Student` class.
"""


class Student:
    """
    A class used to represent a Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the instance attributes to a dictionary representation.
        """
        if (
            isinstance(attrs, list) and
            (all(isinstance(i, str) for i in attrs))
        ):
            newDict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    newDict[key] = value

            return newDict

        return self.__dict__
