#!/usr/bin/python3
"""  function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def append_write(filename="", text=""):
    """ open file, permission for write, and write"""
    with open(filename, 'a', encoding="utf8") as f:
        return (f.write(text))
