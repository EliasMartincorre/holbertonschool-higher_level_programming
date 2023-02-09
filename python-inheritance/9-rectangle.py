#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        return(self.width * self.height)

    def __str__(self):
        string = f"[Rectangle] {self.width}/{self.height}"
        return string
