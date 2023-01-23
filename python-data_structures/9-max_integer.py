#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    a = - 30000
    for item in range(len(my_list)):
        if a < my_list[item]:
            a = my_list[item]
    return a
