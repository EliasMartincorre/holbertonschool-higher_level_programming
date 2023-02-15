#!/usr/bin/python3
""" import module base
    inherit for rectangle"""
from models.base import Base

""" class Rectangle for especific
 comportamiento"""


class Rectangle(Base):
    """ Class rectangle is """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def display(self):
        """ print in stdout a representation
            of th rectangle with #"""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            [print("#" * self.__width)]

    def __str__(self):
        """ information for developer"""
        p1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        p2 = f" - {self.__width}/{self.__height}"
        return p1 + p2

    def area(self):
        """ return the area of the class"""
        return (self.__width * self.__height)

    def update(self, *args):
        """asignacion dinamica de variables"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
