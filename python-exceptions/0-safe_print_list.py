#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(0, x):
            a += 1
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        print()
        return (a - 1)
