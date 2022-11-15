#!/usr/bin/python3
""" sends a post request to an API """
import requests
from sys import argv

if __name__ == "__main__":
    """ This posts to the api"""
    if len(argv) < 2:
        value = ""
    else:
        value = argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")

    try:
        print("[{}] {}".format(data['id'], data['name']))
    except KeyError:
        print("No result")
