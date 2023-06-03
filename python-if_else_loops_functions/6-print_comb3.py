#!/usr/bin/python3

for i in range(0, 10):
    for a in range(0, 10):
        if (i == 8 and a == 9):
            print("{}{}".format(i, a))
        elif (i < a):
            print("{}{}, ".format(i, a), end="")
