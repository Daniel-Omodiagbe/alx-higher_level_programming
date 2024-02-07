#!/usr/bin/python3
"""This module defines the square class based on 2-square.py"""


class Square:
    """class that defines a square with private instance
    attributes size and position. size must be an integer
    position must be a tuple with two values
    exceptions will also be handled"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiation of attributes"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the attribute position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
