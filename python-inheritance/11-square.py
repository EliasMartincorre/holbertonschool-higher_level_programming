#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Ins"""

    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self):
        return(self.__size * self.__size)

    def __str__(self):
        string = f"[Square] {self.__size}/{self.__size}"
        return string
