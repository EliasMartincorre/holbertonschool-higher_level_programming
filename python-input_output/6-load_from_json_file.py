#!/usr/bin/python3
"""import the json library"""


import json
"""function that creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """ return  object"""
    with open(filename, encoding="utf8") as f:
        arc = f.read()
        return json.loads(arc)
