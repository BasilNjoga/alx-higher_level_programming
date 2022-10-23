#!/usr/bin/python3
""" This script fetches a url """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()

print('Body response:')
print("\t - type: {}".format(html))
print("\t - content: {}".format(html))
print("\t - utf8 content: {}".format(html))
