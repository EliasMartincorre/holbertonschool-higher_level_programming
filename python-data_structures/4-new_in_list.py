#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    lista = []
    for i in range(len(my_list)):
        if i < idx:
            lista.append(my_list[i])
        if i == idx:
            lista.append(element)
        if i > idx and i < len(my_list):
            lista.append(my_list[i])
    return lista
