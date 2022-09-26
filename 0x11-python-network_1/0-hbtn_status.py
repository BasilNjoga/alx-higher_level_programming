#!/usr/bin/python3
""" This script fetches a url """
import urllib.request

if __name__ == "__main__":
    with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()


