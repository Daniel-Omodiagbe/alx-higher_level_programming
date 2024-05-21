#!/usr/bin/python3
"""module for from_json_string"""

import json


def from_json_string(my_str):
    """deserializes a json file to dictionary"""
    return json.loads(my_str)
