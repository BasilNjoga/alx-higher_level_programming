#!/usr/bin/python3
"""
This is a modole on python input outputs 
along with json decoding and encoding
"""
import json


def from_json_string(my_str):
    """
    This is a function that returns a json
    representation of a string in object form
    """
    return json.loads(my_str)
