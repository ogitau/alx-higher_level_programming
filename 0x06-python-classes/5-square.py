#!/usr/bin/python3
"""initializes a class square"""


class Square:

    """creates a class square"""

    def __init__(self, size=0):

        """initalizes attributes of square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """checks if condition is not int is met and raises error if not"""

        if (size < 0):
            raise ValueError("size must be >= 0")

        """checks if condition > 0 is met and raises error if not"""

        self.__size = size

    @property
    def size(self):

        """getter for the size"""

        return self.__size

    @size.setter
    def size(self, value):

        """validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """setter for value"""

        if value < 0:
            raise ValueError("size must be >= 0")

        """"size must be >= 0"""

        self.__size = value

    def area(self):
        """calculates the area"""

        return (self.__size ** 2)

    def my_print(self):
        """print # in the square"""

        if self.__size == 0:
            print()
            """print empty line if square is zero"""

        else:
            for i in range(self.__size):
                print("#" * self.__size)

                """actual printing"""
