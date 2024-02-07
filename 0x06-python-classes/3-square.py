#!/usr/bin/python3
"""This module defines the square class based on 2-square.py"""


class Square:
    """class that defines a square with private instance
    attribute size and instantiation with size
    size must be an integer, exceptions will also be handled"""
    def __init__(self, size=0):
        """instantiation of attributes"""
        self.size = size

    @property
    def size(self):
        """getting size"""
        return self.__size

    @size.setter
    def size(self, x):
        """sets the size attribute"""
        if type(x) is not int:
            raise TypeError("size must be an integer")
        if x < 0:
            raise ValueError("size must be >= 0")
        self.__size = x

    def area(self):
        """returns the current area of the square"""
        return self.__size * self.__size
