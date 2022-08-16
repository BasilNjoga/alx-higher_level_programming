#!/usr/bin/python3

"""
This is a module based on 0-rectangles.pym that contains a class that defines a rectangle
giving it's height and width

Attributes:
    __init__ : first instance 

"""

class Rectangle:
    """
    This is a class that defines a rectangle giving 
    it's width and heigth

    Attributes:
        __init__: first instance

    Args:
        self:
    """
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width
        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height
        @height.setter
        def height(self, height):
            self.__height = height