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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """update es una funcion que
        asigna un nuevo valor
        a los atributos de una funcion,
        primero utilizando args, y despues
        utilizando el par-llave
        valor"kwargs"
        """
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.size = args[1]
        if len(args) == 3:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """sumary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
