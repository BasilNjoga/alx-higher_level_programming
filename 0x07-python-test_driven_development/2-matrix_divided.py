#!/usr/bin/python3

"""
This is a module about matrix divided and includes a single
function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    It divides a two dimensional matrix by a factor v
    and returns a new matrix with the new values
    Args:
        matrix: The two dimensional matrix
        div:number to be divided by
    """
    err = "matrix must be a matrix(list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    new_matrix = list(map(list, matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return new_matrix
