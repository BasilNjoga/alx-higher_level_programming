#!/usr/bin/python3
""" This is a module that lists all the attributes and methods of an object """


def lookup(obj):
    """This is a function that returns a list of all attributes
    and methods of the passed object"""
    return dir(obj)
