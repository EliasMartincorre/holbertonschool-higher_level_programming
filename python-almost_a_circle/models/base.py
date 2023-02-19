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

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json"""
        if list_dictionaries is None:
            s = "[]"
            return s
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ list_objs is a list of instances
            who inherits of Base - example:
            list of Rectangle or list of Square instances"""
        stringj = cls.to_json_string([i .to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as filej:
            filej.write(stringj)
