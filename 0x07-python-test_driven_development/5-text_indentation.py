#!/usr/bin/python3

"""
This is a module on text indentation, it contains a
single function text indentations which adds a new line
upon getting to a certain character
"""


def text_indentation(text):
    """
    This is function that prints out a string
    adding indentations when a fullstop,
    question mark or collon is encountered
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print("{:s}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
