#!/usr/bin/python3
"""Implements a Rectangle class from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of class BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns info about the rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
