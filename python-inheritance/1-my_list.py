#!/usr/bin/python3
"""
En este script se crea una clase
llamada MyList que hereda
de la clase list.
"""


class MyList(list):
    """New class for
    this program
    """
    def print_sorted(self):
        """
        Return: return cloning list in order
        """
        print(sorted(self))
