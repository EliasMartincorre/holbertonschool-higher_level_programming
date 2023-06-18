#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


class Rectangle:
    """
        only pass
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ return area rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ perimeter"""
        if (self.__width <= 0) or (self.__height <= 0):
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(f"{self.print_symbol}" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif (rect_1.area() < rect_2.area()):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return (Rectangle(size, size))
