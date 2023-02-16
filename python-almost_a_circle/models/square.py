#!/usr/bin/python3
""" import module base
    inherit for rectangle"""
from models.rectangle import Rectangle

""" class Rectangle for especific
 comportamiento"""


class Square(Rectangle):
    """ Class rectangle is """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ information for developer"""
        p1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        p2 = f" - {self.size}"
        return p1 + p2

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        self.__height = value
