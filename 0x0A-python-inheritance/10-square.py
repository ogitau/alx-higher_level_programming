#!/usr/bin/python3
""" My Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits from class rectangle"""
    def __init__(self, size):
        """initialization of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
