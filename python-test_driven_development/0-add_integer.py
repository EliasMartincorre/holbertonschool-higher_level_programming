#!/usr/bin/python3
"""Holberton School."""


def add_integer(a, b=98):
    """Add an integer."""
    if not isinstance((a), (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance((b), (int, float)):
        raise TypeError("b must be an integer")
    if type(b) == float:
        b = int(b)
    if type(a) == float:
        a = int(a)
    return (a + b)
