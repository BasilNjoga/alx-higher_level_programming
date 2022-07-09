#!/usr/bin/python3
"""
This is a module on input and output functions in python
this module contains a single function read_file that
prints out the contents of a file
"""


def read_file(filename=""):
    """
    This module simply prints out the
    contents of a file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
