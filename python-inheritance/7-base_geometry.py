#!/usr/bin/python3
""" Empty class"""


class BaseGeometry:
    """emppty"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.n = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.v = value
