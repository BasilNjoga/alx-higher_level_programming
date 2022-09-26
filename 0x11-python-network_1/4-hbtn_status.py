#!/usr/bin/python3
""" This is  script that fetches a url using requests """
import requests
r = requests.get('https://alx-intranet.hbtn.io/status', auth=('user', 'pass'))
