#!/usr/bin/python3
"""
This module provides a function to  divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    """

    # Check for the first matrix error
    mat_valid = isinstance(matrix, list)
    if mat_valid:
        mat_valid = len(matrix) > 0
    if mat_valid:
        for i in matrix:
            if not isinstance(i, list):
                mat_valid = False
                break
            for j in i:
                if not isinstance(j, (int, float)):
                    mat_valid = False
                    break
    if not mat_valid:
        raise TypeError(
            "matrix must be a matrix (list of lists) " + "of integers/floats"
        )

    # Check for the second matrix error
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check for the first div error
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    # Check for the second div error
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Do operation
    new_mat = []
    for i in matrix:
        new_mat.append(list(map(lambda j: round(j / div, 2), i)))

    return new_mat
