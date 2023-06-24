#!/usr/bin/python3
"""
 function that writes an Object to a text file,
 using a JSON representation
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    Keyword arguments:
    argument -- object of python. file.json
    Return: file writen.
    """

    with open(filename, 'w', encoding="utf8") as f:
        return (dump(my_obj, f))
