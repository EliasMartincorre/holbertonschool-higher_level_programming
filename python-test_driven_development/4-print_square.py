#!/usr/bin/python3
""""
    print square
"""


def print_square(size):
    if isinstance(size, (int)):
        if (size < 0):
            raise ValueError("size must be >= 0")
        for x in range(size):
            print("#" * size)
    else:
        raise TypeError("size must be an integer")
