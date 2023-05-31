def print_last_digit(number):
    if (number >= 0):
        print(f"{number % 10}", end="")
        return(number % 10)
    if (number < 0):
        print(f"{10 - (number % 10)}", end="")
        return(10 - (number % 10))
