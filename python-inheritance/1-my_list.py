#!/usr/bin/python3
"""
This module defines a custom list class `MyList`
that inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        copied = self.copy()
        copied.sort()
        print(copied)
