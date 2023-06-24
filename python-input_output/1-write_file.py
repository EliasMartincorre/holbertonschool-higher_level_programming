#!/usr/bin/python3
""" module.doc
"""


def write_file(filename="", text=""):
    """
    argument -- file.txt and string.
    Return: returns the number of characters written.
    """

    with open(filename, 'w', encoding='UTF8') as f:
        return (f.write(text))
