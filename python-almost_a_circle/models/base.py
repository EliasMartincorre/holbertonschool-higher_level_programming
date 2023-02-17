#!/usr/bin/python3
""" This class will be the “base” of all other classes"""
import json

class Base:
    """only class Base, count number of instance in id = None"""

    nb_objects = 0

    def __init__(self, id=None):
        """ahora si"""
        if id is None:
            Base.nb_objects += 1
            self.id = self.nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """dictionary to json"""
        a = []
    for i in list_dictionaries:
        a = json.dumps(i)
    return a
