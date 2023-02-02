#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance((div), (int, float)):
        raise TypeError("div must be a number")
    if not isinstance((matrix), (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    n_m = []
    for i in matrix:
        if len(i) == len(matrix[0]):
            n_m.append([round(i[r] / div, 2) for r in range(len(i)) if type(i[r]) == int])
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return n_m
