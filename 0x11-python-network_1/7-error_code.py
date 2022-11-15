#!/usr/bin/python3
""" This script sends a a request and displays the status code """
import requests
from sys import argv

r = requests.get(argv[1])
print("Error code: {}".format(r.status_code))
