#!/usr/bin/python3
"""This module defines the square class based on 0-square.py"""


class Square:
    """class that defines a square with private instance
    attribute size and instantiation with size"""
    def __init__(self, size):
        """instantiation of attributes"""
        self.__size = size
