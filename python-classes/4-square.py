#!/usr/bin/python3
""" this class define a class square"""


class Square:
    """ this attribute define a
        some value allowed for size,
        type anda nonnegative"""

    def get__size(self):
        return self.size

    def set_size(self, value):
        if type(size) != int:
            raise TypeError('size must be an integer')
        self.size = value

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size

    def area(self):
        if type(self.size) != int:
            raise TypeError('size must be an integer')
        return (self.size ** 2)
