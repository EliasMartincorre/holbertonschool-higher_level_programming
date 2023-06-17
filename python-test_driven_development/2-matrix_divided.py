#!/usr/bin/python3
""" this function divide al elements by matrix
    and return  the result"""


def matrix_divided(matrix, div):
    """test all possible case
       when succes and when failed"""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance((div), (int, float)):
        raise TypeError("div must be a number")
    if not isinstance((matrix), (list)):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    n_m = []
    for ls in matrix:
        if len(ls) == len(matrix[0]):
            for a in range(len(ls)):
                if not isinstance((ls[a]), (int, float)):
                    raise TypeError("matrix must be a matrix"
                                    "(list of lists) of integers/floats")
            else:
                n_m.append([round(ls[r] / div, 2) for r in range(len(ls))])
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return n_m
