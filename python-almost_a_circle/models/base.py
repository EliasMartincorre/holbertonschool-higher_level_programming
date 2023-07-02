#!/usr/bin/python3
"""
sera por esto
"""
from json import dumps


class Base:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json represetation of
        python object"""
        lista = []
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)
