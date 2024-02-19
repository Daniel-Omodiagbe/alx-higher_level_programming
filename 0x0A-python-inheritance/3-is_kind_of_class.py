#!/usr/bin/python3
"""explains the use of isinstance"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of
    an object"""
    if isinstance(obj, a_class):
        return True
    return False
