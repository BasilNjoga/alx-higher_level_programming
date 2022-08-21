#!/usr/bin/python3
""" This is a class that inherits from the Base module """
from models.base import Base


class Rectangle(Base):
    """ This is a class that inherits from base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ This is a function that computes area """
        return (self.__width * self.__height)

    def display(self):
        """ This is a funciton that prints a rectangle with # """
        for y in range(self.__y):
            print("\n", end="")
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for i in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __repr__(self):
        output = ("[Rectangle] (" + str(self.id) + ")" + " " + str(self.__x))
        output += ("/" + str(self.__y) + " " + "-" + " ")
        output += (str(self.__width) + "/" + str(self.__height))
        return output
