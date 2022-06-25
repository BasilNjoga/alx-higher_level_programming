#!/usr/bin/python3

"""
This is a module on adding two integers

it has a single function, add_integers() which adds two integers

"""

def add_integer(a, b=98):
    """
    it adds two integers and returns the sum

    """
    if type(a) is not int :
        raise TypeError("a must be an integer")
    elif type(b) is not int :
        raise TypeError("b must be an integer")
    return a + b

print(add_integer(1, 2))