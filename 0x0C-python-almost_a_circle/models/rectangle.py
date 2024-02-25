#!/usr/bin/python3
"""defines the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """inherits the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assign a value to width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign a value to width attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the width"""
        return self.__x

    @x.setter
    def x(self, value):
        """assign a value to width attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the width"""
        return self.__y

    @y.setter
    def y(self, value):
        """assign a value to width attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value