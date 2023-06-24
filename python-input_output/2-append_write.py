#!/usr/bin/python3
"""
Keyword arguments:
argument -- file.txt and string.
"""


def append_write(filename="", text=""):
    """
    function that appends
    a string at the end of a text file (UTF8)
    Return: returns the number of characters added:
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
