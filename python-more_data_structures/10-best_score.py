#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = 0
    b = ""
    for key, value in a_dictionary.items():
        if a < value:
            a = value
            b = key
    return b
