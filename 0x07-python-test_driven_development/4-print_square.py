#!/usr/bin/python3

"""
This is a module of print square and it has a single function
print square which prints a square

"""


def print_square(size):
    """
    This is function that prints a square based
    on the size of variable given in size
    Args:
        size: size of the variable
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, int):
        raise ValueError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("\n", end="")
