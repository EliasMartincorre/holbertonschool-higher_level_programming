#!/usr/bin/python3
""" whats your name """


def say_my_name(first_name, last_name=""):
    """ different possible"""
    if type(first_name) == str and type(last_name) == str:
        print("My name is {} {}".format(first_name, last_name))
    if type(first_name) != str and type(last_name) == str:
        raise TypeError("first_name must be a string")
    if type(first_name) == str and type(last_name) != str:
        raise TypeError("last_name must be a string")
