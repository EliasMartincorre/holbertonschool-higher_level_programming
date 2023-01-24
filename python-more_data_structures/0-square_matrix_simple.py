#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return 0
    new_matrix = []
    for i in matrix:
        new_matrix.append([i[row] ** 2 for row in range(len(i))])
    return new_matrix
