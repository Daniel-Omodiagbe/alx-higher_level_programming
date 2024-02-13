#!/usr/bin/python3
"""defines the class rectangle"""


class Rectangle:
    """ defines a rectangle based on 1-rectangle
    with width and height as attribute"""

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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
