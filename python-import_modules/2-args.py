#!/usr/bin/python3
if __name__ == '__main__':
    """Este programa implemmentara 
    la importacion de modulo sys, para hacer uso 
    del metodo argv, el cual nos permite tomar
    un valor de entrada igresado por el usuario
    y realizarle una serie de pasos para obtener 
    un resultado, para este programa se exige
    que solo se ejecute el programa si lo invocamos 
    como principal '__main__, en los casos 
    donde se importasels
      __name__ =  <nombredelmodulo>.
      Este programa contara las cantidad 
      de argumentos ingresados y los devolvera
      en la pantalla.

    """   
    from sys import argv
a = (len(argv))
if a == 2:
    print("{} argument:".format(a - 1))
elif a == 1:
    print("{} arguments.".format(a - 1))
else:
    print("{} arguments:".format(a - 1))
for i in range(1, a):
    print("{}: {}".format(i, argv[i]))
