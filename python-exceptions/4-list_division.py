#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlista = []
    div = 0
    for i in range(list_length):
        try:
            div = float(my_list_1[i] / my_list_2[i])
            newlista.append(div)
        except ZeroDivisionError:
            pass
            print("division by 0")
            newlista.append(0)
        except TypeError:
            pass
            print("wrong type")
            newlista.append(0)
        except IndexError:
            print("out of range")
            newlista.append(0)
        finally:
            pass
    return newlista
