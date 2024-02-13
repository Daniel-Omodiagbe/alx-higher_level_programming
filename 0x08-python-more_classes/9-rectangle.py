#!/usr/bin/python3
"""defines the class rectangle"""


class Rectangle:
    """ defines a rectangle based on 1-rectangle
    with width and height as attribute"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation of class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ prints the rectangle with # characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        print_str = []
        for i in range(self.__height):
            print_str.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                print_str.append("\n")
        return "".join(print_str)

    def __repr__(self):
        """returns string representation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instance of the class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.perimeter() >= rect_2.perimeter():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance with width=height=size"""
        width = size
        height = size
        return cls(width, height)
