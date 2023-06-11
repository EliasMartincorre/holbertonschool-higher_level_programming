#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for key, value in a_dictionary.items():
        new_d[key] = value * 2
    return new_d
