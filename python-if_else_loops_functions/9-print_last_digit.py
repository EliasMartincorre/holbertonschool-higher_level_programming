#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = number % 10
    if number < 0:
        lastdigit = 10 - lastdigit
    print(lastdigit, end="")
    return(lastdigit)
