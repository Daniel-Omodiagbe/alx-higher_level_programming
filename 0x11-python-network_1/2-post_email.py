#!/usr/bin/python3
"""
Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
"""

import urllib.request as urll
import sys
import urllib.parse as parse


if __name__ == "__main__":
    value = parse.urlencode({email: sys.argv[2]})
    value = value.encode('utf-8')
    with urll.urlopen(sys.argv[1], value) as res:
        print(res.read().decode('utf-8'))
