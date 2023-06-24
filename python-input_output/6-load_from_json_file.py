#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""
from json import load


def load_from_json_file(filename):
    """
    Keyword arguments:
    argument -- file.json
    Return: object python.
    """
    with open(filename) as f:
        return (load(f))
