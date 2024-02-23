#!/usr/bin/python3
"""A base class BaseGeometry"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """that raises an Exception with the message area()
        is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of attributes"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-baseGeometry.txt")
