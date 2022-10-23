#!/usr/bin/python3
""" This script takes a url and email and sends a post request """

from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    """ reads as a file """
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html.decode('utf-8'))
