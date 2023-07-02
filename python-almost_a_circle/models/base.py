#!/usr/bin/python3
"""
sera por esto
"""
from json import dumps, loads


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

    @classmethod
    def save_to_file(cls, list_objs):
        b = []
        if list_objs is None:
            a = "[]"
        else:
            for objetos in list_objs:
                b.append(objetos.to_dictionary())
            a = cls.to_json_string(b)
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            f.write(a)

    @staticmethod
    def from_json_string(json_string):
        """
            Keyword arguments:
            argument: json_string is a string representing
            a list of dictionaries
            Return: return_description
            """
        if json_string is None:
            return []
        else:
            return loads(json_string)
