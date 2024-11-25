#!/usr/bin/python3
"""
This module provides a function to print a square
"""


def print_square(size):
    """
    Print a square with the character '#'.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
