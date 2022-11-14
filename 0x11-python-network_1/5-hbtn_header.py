#!/usr/bin/python3
""" This is  script that fetches a url using requests """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if (r.headers['X-Request-Id'] == False):
        print(None)
    else:
        print(r.headers['X-Request-Id'])
