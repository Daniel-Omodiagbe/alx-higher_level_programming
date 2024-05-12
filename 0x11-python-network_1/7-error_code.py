#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the UR
 and displays the body of the response (decoded in utf-8)
"""

import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
