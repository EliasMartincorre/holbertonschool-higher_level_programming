#!/usr/bin/python3
""" class square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ area"""
        return(self.__size * self.__size)

    def __str__(self):
        """  ff """
        return (f"[Square] {self.__size}/{self.__size}")
