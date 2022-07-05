#!/usr/bin/python3

"""
This is a module on python input outputs
This file has a single function that reads data
from a text file
"""


def read_file(filename=""):
    """
    This program simply reads text from a file
    Args:
        filename: contains the name of the file
    """
    with open(filename, encoding="UTF8") as f:
        read_data = f.read()
        print("{:s}".format(read_data))
