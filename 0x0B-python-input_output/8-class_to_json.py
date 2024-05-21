#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    if type(obj) is obj.__class__:
        return (obj.__dict__)
