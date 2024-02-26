#!/usr/bin/python3
"""defines the square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits the rectangle module"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of instance attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
