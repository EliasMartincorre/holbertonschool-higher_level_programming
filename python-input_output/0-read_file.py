#!/usr/bin/pythoon3
"""
 function that reads a text
 file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Keyword arguments:
    argument -- filename.txt
    Return: all character in the
    file.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read())
