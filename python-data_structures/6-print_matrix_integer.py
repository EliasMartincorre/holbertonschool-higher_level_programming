#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return None
    for row in matrix:
        for i in range(len(row)):
            print("{}".format(row[i]), end=" ")
        print()
