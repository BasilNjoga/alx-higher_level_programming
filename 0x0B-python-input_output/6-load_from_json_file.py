#!/usr/bin/python3
"""
This is a moudule on reading an object from
a json file
"""
import json


def load_from_json_file(filename):
    """
    This is a function that loads an object
    from a json file given
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
