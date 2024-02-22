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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-baseGeometry.txt")
