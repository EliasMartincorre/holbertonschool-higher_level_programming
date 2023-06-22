#!/usr/bin/python3
"""
esta funcion return true si
el objeto es una instancia de la clase
o si hereda de ella
"""


def is_kind_of_class(obj, a_class):
    """
    argument -- obj: object, a_class = class
    Return: true or false
    """
    return isinstance(obj, a_class)
