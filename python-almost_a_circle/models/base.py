#!/usr/bin/python3
""" This class will be the “base” of all other classes"""
import json
import os


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
        if list_objs is None:
            strj = "[]"
        else:
            strj = cls.to_json_string([i .to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as filej:
            filej.write(strj)

    def from_json_string(json_string):
        """that returns the list of the JSON str representation json_string"""
        if json_string is None:
            a = []
            return a
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create devuelve una instancia con todos los metodos
            ya establecidos"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instance from json file"""
        a = cls.__name__ + ".json"
        if os.path.exists(a):
            with open(a) as filej:
                b = cls.from_json_string(filej.read())
                return [cls.create(**i) for i in b]
        else:
            b = []
            return b
