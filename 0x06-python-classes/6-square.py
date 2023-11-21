#!/usr/bin/python3
"""initializes a class square"""


class Square:

    """creates a class square"""

    def __init__(self, size=0, position=(0, 0)):

        """initalizes attributes of square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """checks if condition is not int is met and raises error if not"""

        if (size < 0):
            raise ValueError("size must be >= 0")

        """checks if condition > 0 is met and raises error if not"""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):

        """getter for the position"""

        return self.__position

    @position.setter
    def size(self, value):

        """validation"""

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise ValueError("positive must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple pf 2 positive integes")
        else:
            """"position must be a tuple of 2 positive integers"""

        self.__position = value

    def area(self):
        """calculates the area"""

        return (self.__size ** 2)

    def my_print(self):
        """print # in the square"""

        if self.__size == 0:
            print()
            """print empty line if square is zero"""

        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
            for i in range(self.__size):
                print("#" * self.__size)

                """actual printing"""
