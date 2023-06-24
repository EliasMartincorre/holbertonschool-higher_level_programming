#!/usr/bin/python3
"""
class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
Instantiation with first_name,
last_name and age:
def __init__(self, first_name, last_name, age):

"""


class Student:
    """Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """Return: dictionary representation of the instances
        recupera una representacion del diccionario

        """
        dic = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    dic[key] = value
        else:
            dic = self.__dict__
        return dic
