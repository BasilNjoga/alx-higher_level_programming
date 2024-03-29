#!/usr/bin/python3
""" This script takes a url and displays the value of a header """

from sys import argv
import urllib.request

if __name__ == "__main__":
    """ returns response as a file """
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()

    print(response.getheader("X-Request-Id"))
