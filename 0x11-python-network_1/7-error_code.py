#!/usr/bin/python3
""" This script sends a request to the URL and displays the body of the response """
import requests
from sys import argv

r = requests.get(argv[1])
if (r.status_code >= 400):
    print("Error: {}".format(r.status_code))
else:
    print(r.text)
