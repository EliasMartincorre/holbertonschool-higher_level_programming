#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if len(a) < 2:
        a.append(0)
        if len(a) < 2:
            a.append(0)
    if len(b) < 2:
        b.append(0)
        if len(b) < 2:
            b.append(0)
    c = [0, 0]
    c[0] = a[0] + b[0]
    c[1] = a[1] + b[1]
    return tuple(c)
