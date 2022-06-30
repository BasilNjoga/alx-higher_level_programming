#!/usr/bin/python3

"""
This is a module on adding two integers

it has a single function, add_integers() which adds two integers

"""

def add_integer(a, b=98):
    """
    it adds two integers and returns the sum

    """
    if isinstance(a,str):
        raise TypeError("a must be an integer")
    if isinstance(b,str):
        raise TypeError("b must be an integer")
    return int (a + b)
