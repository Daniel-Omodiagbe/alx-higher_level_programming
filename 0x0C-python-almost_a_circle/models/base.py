#!/usr/bin/python3
"""the first class Base"""


class Base:
    """this class is the base of other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
