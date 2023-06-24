#!/usr/bin/pythoon3
"""
 function that reads a text
 file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Return: all character in the
    file.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        tostdout = f.read()
        print(tostdout, end='')
