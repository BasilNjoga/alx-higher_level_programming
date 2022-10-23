#!/usr/bin/python3

from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()

print(html.decode(X-Request-Id))
