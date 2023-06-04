># Python - import & modules


## 0-add.py
* This program will imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 </li>
<br>

## 1-calculation.py
* This program import functios from file calculator_1.py does some Maths, and prints the result
<br>

## 2-args.py
* This program will prints the number of the list of its arguments

## 3-infinite_add.py
* This program prints the result of addition of all arguments 
<br>

## 4-hidden_discovery.py
 * Program that prints all the names defined by the compiled module hidden_4.pyc
 <br>

 ## 5-variable_load.py
 * This program imports the variable a from the file variable_load_5.py and prints its value.
</ul>

 > # Learning Objectives

 ### How to import functions from another file:
 * Hay dos formas de hacerlo importando todo el espacio de nombres del modulo importado,(import <--nombremodulo-->) o importando al espacio de nombres del programa solo lo que precisamos importar. (from <--nombredemodulo--> import <--algo-->). Hay un tercer metodo que utilizando la funcion 
 ' __import__() .'

### How to use imported functions
* Si se importo el modulo entero con import <--nombremodulo-->
se utilizara la expresion <--nombredelmodulo-->.<--nombredelainstruccion-->(). 
O si se importo solo el objeto a utilizar, basta con utilizar la funcion como si perteneciera al espacio de nombres. 

### How to create a module
* Para crear un modulo debemos crear un archivo con una estencion .py. .

### How to use the built-in function dir()
* Para utilizar la funcion dir(). Simplemente la ejecutamos 
pasandole como parametro el objeto donde queremos conocer el espacio de nombres.

### How to prevent code in your script from being executed when imported
para prevenir que un script se ejecute cuando lo importamos 
simplemente lo encapsulamos con la clausura " if __name__ = "__main": . Si el script no se ejecuta como main, es decir fue importado, todo lo que esta dentro de la clusula no se ejecutara. 

### How to use command line arguments with your Python programs
* Para poder hacer uso de la linea de argumentos se puede utilizar el modulo sys , dentro del mismo la funcion argv. Esta funcion nos returnara una lista de todos los argumentos ingresados separados por un caracter de " ".
