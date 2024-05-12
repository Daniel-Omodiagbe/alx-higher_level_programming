#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the UR
 and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request as urll
import urllib.error


if __name__ == "__main__":
    req = urll.Request(sys.argv[1])
    try:
        with urll.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
