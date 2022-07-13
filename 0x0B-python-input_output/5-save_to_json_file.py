#!/usr/bin/python3
"""
This is a module that writes an object to a python
file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This is a function that writes an object to a json
    file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dump(my_obj))
