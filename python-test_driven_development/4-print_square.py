#!/usr/bin/python3
""" define a square, whit size input"""


def print_square(size):
    """ exception for the incorrectly argument"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
