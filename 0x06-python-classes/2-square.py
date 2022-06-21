#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is a module containing a class square
This class only has attributes at the present

Attributes:
    class Square

"""


class Square:
    """an empty Square class

    Attributes:
        attr1 : size
            size of the square

    Args:
        None
    """
    def __init__(self, size=0):
        """
        parameters:

        param1 : size
            this is the size of the square which in this case is protected
        """
        self.__size = size
        try:
            k = size / 3
            assert size >= 0
        except TypeError:
            print("size must be an integer")
            raise
        except AssertionError:
            print("size must be >= 0")
            raise
