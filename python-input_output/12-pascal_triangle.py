#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n + 1):
        if i == 0:
            continue
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                num1 = triangle[i - 2][j - 1]
                num2 = triangle[i - 2][j]
                row.append(num1 + num2)

        triangle.append(row)

    return triangle
