#!/usr/bin/python3
if __name__ == '__main__':
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
