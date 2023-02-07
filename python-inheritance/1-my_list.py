#!/usr/bin/python3
""" Example of classinheritance"""


class MyList(list):
    """ print sorted list and no change anything"""
    def print_sorted(self):
        print(sorted(self))
