#!/usr/bin/python3
"""
Keyword arguments:
argument -- adition
Return: adition of a and b
"""
def add_integer(a, b=98):
    """
    Return: adition a +b
    """
    
    if not isinstance((a), (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance((b), (int, float)):
        raise TypeError("b must be an integer")
    if type(b) == float:
        b = int(b)
    if type(a) == float:
        a = int(a)
    return (a + b)
