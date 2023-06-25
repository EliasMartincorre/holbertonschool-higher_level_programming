#!/usr/bin/python3
"""New class BaseGeometry
"""


class BaseGeometry():
    """empty class
    """

    def area(self):
        """ empty function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "only int"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
