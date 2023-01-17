#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i < k and i < 8:
            print("{}{}".format(i, k), end=", ")
        if k == 9 and i == 8:
            print("{}{}".format(i, k), end=None)
