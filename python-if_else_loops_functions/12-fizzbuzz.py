#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i % 3 != 0 and i % 5 != 0:
            print(i, end=" ")
        elif i % 5 == 0 and i % 3 == 0 and i != 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0 and i != 0:
            print("Buzz", end=" ")
        elif i % 3 == 0 and i != 0:
            print("Fizz", end=" ")
