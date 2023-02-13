#!/usr/bin/python3
""" import the diferent modules to use"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    with open("add_item.json", 'r+') as f:
        a = json.load(f)
except FileNotFoundError:
    a = []

a.extend(sys.argv[1:])
save_to_json_file(a, "add_item.json")
