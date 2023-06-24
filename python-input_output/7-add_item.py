#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
from sys import argv
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
a = []
for i in range(1, len(argv)):
    a.append(argv[i])

if os.path.exists(filename):
    myobjeto = load_from_json_file(filename)
    for i in range(len(a)):
        myobjeto.append(a[i])
    save_to_json_file(myobjeto, filename)
else:
    save_to_json_file(a, filename)
