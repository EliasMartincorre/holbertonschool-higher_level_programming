#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """clase que hereda de
    la clase rectangulo que a su vez
    hereda de ka ckase base,
    se utiliza el metodo super.__init__ para
    utilizar los elementos de la clase
    base."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} {self.size}"
