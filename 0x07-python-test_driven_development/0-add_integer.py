#!/usr/bin/python3

"""
This is a module on adding two integers

it has a single function, add_integers() which adds two integers

"""


def add_integer(a, b=98):
    """
    it adds two integers and returns the sum

    """
    if isinstance (a, float):
        a = int(a)
    if isinstance (b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a + b)
