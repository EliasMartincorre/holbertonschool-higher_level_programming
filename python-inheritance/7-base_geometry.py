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
        """ only int"""
        self.value = value
        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        