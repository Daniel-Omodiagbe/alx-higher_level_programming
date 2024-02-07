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
    def size(self, value):
        """sets the size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
