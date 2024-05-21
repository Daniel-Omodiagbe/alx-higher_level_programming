#!/usr/bin/python3
"""Module for class Student"""

class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student"""
        return self.__dict__
