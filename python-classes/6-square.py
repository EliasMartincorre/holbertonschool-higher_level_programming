#!/usr/bin/python3
"""In this program I created a class with the name
    Square then I`m saving the different features
    that describe a square. 
"""


class Square:
    """ this is a empty class
        for started  to work about
        class

        in the start of this class
        evoke an constructor __init__, 
        the class allow  likes input, two arguments.
        Se hace uso de los decoradores @property y  @setter para 
        reasignar un nuevo valor a una variable creada como privada.


    """
    def __init__(self, size=0, position=(0, 0)):
        """the metodo init inicializa una clase con
        ciertos valores, pero en este caso se crea
        el atributo size como privado
        para que pertenezca a la clase
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Este es un metodo
        de instancia que toma el valor
        de size devuelve el cuadrado.
            """
        return (self.__size ** 2)

    def my_print(self):
        """
            print in stdout a
            graphic representation of
            square with character #
            """
        if self.__size == 0:
            print()
        for b in range(0, self.__position[1]):
            print()
        for i in range(self.size):
            for c in range(self.__position[0]):
                print("", end=" ")
            for a in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(self.__position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
