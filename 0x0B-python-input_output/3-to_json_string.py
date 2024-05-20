#!/usr/bin/python3
"""module for to_json_string function"""

import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)"""
    if my_obj:
        if len(my_obj == 0):
            return my_obj
        return json.dumps(my_obj)
