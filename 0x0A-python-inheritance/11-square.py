#!/usr/bin/python3
""" My Square module"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """class square inherits from class rectanglr"""
    def __init__(self, size):

        """initialization of size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the string representation of the square"""

        return "[square] {}/{}".format(self.__size, self.__size)
