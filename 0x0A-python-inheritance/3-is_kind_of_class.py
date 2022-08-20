#!/usr/bin/python3
""" This checks for an instance or inheritance of an object """


def is_kind_of_class(obj, a_class):
    """ This fucntion checks for an instance and inheritance """
    if isinstance(obj, a_class):
        return True
    else:
        return False
