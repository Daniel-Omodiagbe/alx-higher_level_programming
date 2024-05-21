#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student"""
        attrs_dict = {}
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                for i in attrs:
                    if hasattr(self, i):
                        attrs_dict[i] = getattr(self, i)
                return attrs_dict
        return self.__dict__
