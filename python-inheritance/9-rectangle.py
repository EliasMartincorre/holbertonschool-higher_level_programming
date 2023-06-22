#!/usr/bin/python3
""" new class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ base inherits of Basegeometry"""
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """  area """
        return (self.__height * self.__width)

    def __str__(self):
        return (f"[{__class__.__name__}] {self.__width}/{self.__height}")
