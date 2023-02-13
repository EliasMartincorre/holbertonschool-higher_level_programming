#!/usr/bin/python3
""" this module become object in string.json"""

import json
""" take a string.json and return python object"""


def from_json_string(my_str):
    """to object"""
    return json.loads(my_str)
