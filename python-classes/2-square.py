#!/usr/bin/python3
""" this class define a class square"""


class Square:
    """ this attribute define a
        some value allowed for size,
        type anda nonnegative"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an interger')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__Square__size = size
