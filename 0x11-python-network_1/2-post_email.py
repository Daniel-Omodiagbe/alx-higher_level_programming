#!/usr/bin/python3
"""
Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
"""

import urllib.request as urll
import sys
import urllib.parse as parse


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = urll.Request(url, data)
    with urll.urlopen(req) as res:
        print(res.read().decode('utf-8'))
