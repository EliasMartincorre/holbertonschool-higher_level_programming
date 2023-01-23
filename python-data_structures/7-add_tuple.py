#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_a) > 0:
        tupleop = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) < 2 and len(tuple_b) > 0:
        tupleop = tuple_a[0] + tuple_b[0], tuple_a[1]
        return tupleop
    if len(tuple_b) == 0:
        return tuple_a
    else:
        tupleop = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tupleop
