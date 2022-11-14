#!/usr/bin/python3
""" This script sends a url post request with an email """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
