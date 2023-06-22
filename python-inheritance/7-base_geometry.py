#!/usr/bin/python3
"""Empty class BaseGeometry
"""


class BaseGeometry():
    """empty class
    """
    def __init__(self):
        pass

    def area(self):
        """ empty function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError(f'{name} must be an integer')
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
