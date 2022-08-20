#!/usr/bin/python3
""" This module checks if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ This function checks if obj is an instance of a_class """
    if type(obj) == type(a_class):
        return True
    elif type(obj) == a_class:
        return True
    else:
        return False
