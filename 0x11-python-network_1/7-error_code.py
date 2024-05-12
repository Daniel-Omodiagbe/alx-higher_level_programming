#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the UR
 and displays the body of the response (decoded in utf-8)
"""

import sys
import requests


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"Error code: {req.status_code}")
