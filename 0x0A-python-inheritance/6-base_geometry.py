#!/usr/bin/python3
"""A base class BaseGeometry"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """that raises an Exception with the message area()
        is not implemented"""
        raise Exception("area() is not implemented")
