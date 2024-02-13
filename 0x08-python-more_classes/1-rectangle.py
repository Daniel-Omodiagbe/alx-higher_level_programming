#!/usr/bin/python3
"""
This module defines a rectangle class based on 0-rectangle
The class has two attributes namely: width and height
"""


class Rectangle:
    """ defines a rectangle based on 0-rectangle"""

    def __init__(self, width=0, height=0):
        """ instantiation of class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width attribute """
        if value not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height attribute """
        if value not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
