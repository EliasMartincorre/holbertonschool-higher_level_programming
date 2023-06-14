#!/usr/bin/python3
""" this class define a class square"""


class Square:
    """ this attribute define a
        some value allowed for size,
        type anda nonnegative"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
      
            
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) != int :
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[1] != int):
           raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """sumary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return (self.__size ** 2)

    def my_print(self):
        """sumary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if (self.__size == 0):
            print()
            return
        for i in range(self.__position[1]):
            print("")

        for b in range(self.__size):
            for c in range(self.__position[0]):
                print(" ", end="")
            for d in range(self.__size):
                print("#", end="")
            print()
