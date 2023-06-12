#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


class Square:
    """ this is a empty class
        for started  to work about
        class
    """
    def __init__(self, size=0):
        """the metodo init inicializa una clase con
        ciertos valores, pero en este caso se crea
        el atributo size como privado
        para que pertenezca a la clase
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Este es un metodo
        de instancia que toma el valor
        de size devuelve el cuadrado.
            """
        return (self.__size * self.__size)

    def my_print(self):
        """print in stdout a
        graphic representation of
        square with character #
        """

        if self.size == 0:
            print()
        for i in range(self.size):
            for a in range(self.size):
                print("#", end="")
            print()
