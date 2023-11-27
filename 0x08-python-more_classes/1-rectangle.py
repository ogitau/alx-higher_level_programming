#!/usr/bin/python3
"""the module for my rectangle"""


class Rectangle:
    """ class for rectangle"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - gets the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter - sets the value of width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - gets the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter - sets the value of height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
