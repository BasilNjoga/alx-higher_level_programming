#!/usr/bin/python3
from base import Base


class myclass:

    counter = 0
    def __init__(self, id=None):
        self.id = id
        myclass.counter += 1
        self.__nb_object = myclass.counter
    """
    @property
    def nb_object(self):
        return self.__nb_object
    @nb_object.setter
    def nb_object(self, id)
    """
    def __str__(self):
        return str(self.__nb_object)


b1 = Base()
b2 = Base()
b3 = Base()
print(b3)