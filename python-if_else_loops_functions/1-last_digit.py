#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number} is "
if number > 0 or (number % 10) == 0:
    if (number % 10) > 5:
        print(str + f"{number % 10} and is greater than 5")
    elif (number % 10) == 0:
        print(str + f"{number % 10} and is 0")
    elif (number % 10) < 6:
        print(str + f"{number % 10} and is less than 6 and not 0")
else:
    print(str + f"-{(10 - (number % 10))} and is less than 6 and no 0")
