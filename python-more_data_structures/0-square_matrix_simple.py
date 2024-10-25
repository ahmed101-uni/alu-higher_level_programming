#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for col in matrix[row]:
            new_matrix[row].append(col ** 2)

    return new_matrix
