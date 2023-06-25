#!/usr/bin/python3
""" create a class studen with some argument"""


class Student:
    """ defin public instance attribute"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ self .__dict arguments == None otherwise only key in the list"""
        dic = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    dic[key] = value
        else:
            dic = self.__dict__
        return dic

    def reload_from_json(self, json):
        """ that replaces all
        attributes of the Student instance:
        """

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
