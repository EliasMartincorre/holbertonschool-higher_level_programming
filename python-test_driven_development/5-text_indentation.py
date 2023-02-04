#!/usr/bin/python3
def text_indentation(text):
    if not type(text) == str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ".:?":
            print(text[i], end="\n\n")
        if text[i] == " " and text[i - 1] in ".:?" and i != 0:
            pass
        elif text[i] not in ".:?": 
            print("{:s}".format(text[i]), end="")            
