#!/usr/bin/python3
"""import library json"""


import json
""" function that writes an Object to
a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """ w = write. dumps convert to .json"""
    with open(filename, "w", encoding="utf8") as f:
        return f.write(json.dumps(my_obj))
