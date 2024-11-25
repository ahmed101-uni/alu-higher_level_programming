#!/usr/bin/python3
"""
This module provides a function to print a square
"""


def text_indentation(text):
    """
    prints each segment separated by two newlines.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    portions = [""]
    for i in text:
        if i == " " and len(portions[-1]) == 0:
            continue
        portions[-1] += i
        if i in [".", "?", ":"]:
            portions.append("")

    print("\n\n".join(portions), end="")
