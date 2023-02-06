#!/usr/bin/python3
""" empty class Rectangle"""


class Rectangle:
    """ Represent a rectangle"""
    def __init__(self, width=0, height=0, number_of_instances=1):
        self.width = width
        self.height = height
        type(self).number_of_instances = number_of_instances
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            string = ""
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        else:
            string = ""
        return string

    def __repr__(self):
        return "Rectangle(2, 4)"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
