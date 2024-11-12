#!/usr/bin/python3
"""
This module defines class `MyInt` that inherits from the `int`
type and inverts the behavior of the equality (`==`)
and inequality (`!=`) operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of the built-in int type with
    inverted equality operators.
    """

    def __eq__(self, other):
        """
        inverts the equality operator (==) for the class.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator (!=) for the class.
        """
        return super().__eq__(other)
