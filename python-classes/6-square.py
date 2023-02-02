#!/usr/bin/python3
""" this class define a class square"""


class Square:
    """ this attribute define a
        some value allowed for size,
        type anda nonnegative"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(self.__position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
