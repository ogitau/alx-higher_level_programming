#!/usr/bin/python3
"""initializes a class square"""


class Square:

    """creates a class square"""

    def __init__(self, size=0):

        """initalizes attributes of square"""

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        """checks if condition is not int is met and raises error if not"""

        if (size < 0):
            raise ValueError("size must be >= 0")

        """checks if condition > 0 is met and raises error if not"""

        self.__size = size
        """initializes size as an integer
        checks for several conditions and raises errors if not met"""

        def area(self):
            return self.__size * self.__size
        """finds the area and returns it """
