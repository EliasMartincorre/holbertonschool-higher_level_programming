#!/usr/bin/python3
"""
esta funcion return true si
el objeto hereda directa o indirectamente
de una clase
"""


def inherits_from(obj, a_class):
    """
    argument -- obj: object, a_class = class
    Return: true or false
    """
    if issubclass(a_class, type(obj)):
        return False
    elif issubclass(type(obj), a_class):
        return True
