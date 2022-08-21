#!/usr/bin/python3
"""
This is a module called base that has a single
class base which will be the base of all
future classes
"""


class Base:
    """
    This is a class that contains a private attribute nb_object along with
    public attributes self and None
    """
    nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.nb_object += 1
            self.__nb_object = Base.nb_object
            self.id = self.__nb_object
