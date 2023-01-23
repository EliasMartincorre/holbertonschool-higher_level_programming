#!/usr/bin/python3
def no_c(my_string):
    astr = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            astr += i
    return (astr)
