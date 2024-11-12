#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.
    """

    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
