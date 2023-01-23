#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            lista.append(True)
        else:
            lista.append(False)
    return lista
