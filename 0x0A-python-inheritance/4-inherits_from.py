#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
