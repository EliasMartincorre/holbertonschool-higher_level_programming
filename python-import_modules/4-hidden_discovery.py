#!/usr/bin/python3
if __name__ == "__main__":
    import string
    names = dir(string)
    print(names)
    for i in names:
        if i[:2] != '__':
            print(i)
