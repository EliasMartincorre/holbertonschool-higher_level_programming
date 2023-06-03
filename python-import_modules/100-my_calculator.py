#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a, b, c = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
        if b == "+":
            print("{} + {} = {}".format(a, c, add(a, c)))
            sys.exit(0)
        if b == "-":
            print("{} - {} = {}".format(a, c, sub(a, c)))
            sys.exit(0)
        if b == "/":
            print("{} / {} = {}".format(a, c, div(a, c)))
            sys.exit(0)
        if b == "*":
            print("{} * {} = {}".format(a, c, mul(a, c)))
            sys.exit(0)
        print("Unknow operator. Available operators: +, -, * and /")
        sys.exit(1)
