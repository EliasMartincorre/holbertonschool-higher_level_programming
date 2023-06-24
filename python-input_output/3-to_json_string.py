#!/usr/bin/python3
"""
Keyword arguments:
argument -- description
Return: return_description
"""
from json import dumps


def to_json_string(my_obj):
    """
    argument -- object of python
    Return: object.json
    """
    return (dumps(my_obj))
