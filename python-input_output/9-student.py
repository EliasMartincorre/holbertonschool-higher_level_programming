#!/usr/bin/python3
""" create a class studen with some argument"""


class Student:
    """ defin public instance attribute"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ self .__dict"""
        return self.__dict__
