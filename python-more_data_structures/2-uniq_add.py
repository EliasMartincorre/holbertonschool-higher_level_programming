#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    new = [*set(my_list)]
    for i in new:
        a += i
    return a
