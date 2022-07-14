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
    __nb_object = 0
    def __init__(self,id=None):
        self.__nb_object = 0
        if id == None:
            self.__nb_object += 1
            self.id =self. __nb_object
        else:
            self.id = id
