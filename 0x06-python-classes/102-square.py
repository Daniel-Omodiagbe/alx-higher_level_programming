#!/usr/bin/python3
"""This module defines the square class using the 1-square.py"""


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
    def size(self, value):
        """sets the size attribute"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines the area of the square"""
        return self.__size * self.__size

    def __eq__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size == value.__size
        return False

    def __ne__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size != value.__size
        return False

    def __lt__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size < value.__size
        return False

    def __gt__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size > value.__size
        return False

    def __le__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size <= value.__size
        return False

    def __ge__(self, value):
        """checks for equality of squares"""
        if isinstance(value, Square):
            return self.__size >= value.__size
        return False
