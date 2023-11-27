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

    def __str__(self):
        """returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string

    def __repr__(self):
        """reproduces the string representation of the rectangle"""

        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def area(self):
        """calculates the area of the rectangle"""

        return self.height * self.width

    def perimeter(self):
        """calculates the perimeter of the rectangle"""

        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2
