#!/usr/bin/python3
""" This is  script that fetches a url using requests """
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
