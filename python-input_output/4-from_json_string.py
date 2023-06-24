#!/usr/bin/python3
"""
argument -- object.json
Return: object of python
"""
from json import loads


def from_json_string(my_str):
    """
    Return: object of python
    """

    return (loads(my_str))
