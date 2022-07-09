#!/usr/bin/python3

"""
This is module that appends a string to
the end of a file
"""


def append_write(filename="", text=""):
    """
    This is a function that appends to a
    string
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
