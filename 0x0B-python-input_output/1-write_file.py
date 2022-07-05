#!/usr/bin/python3

"""
This is module on writing a file
it contains a single file 1-write_file.py
which writes to a file
"""

def write_file(filename="", text=""):
    """
    function that writes to a file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
