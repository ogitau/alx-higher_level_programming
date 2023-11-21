#!/usr/bin/python3
"""instantiates a class"""


class Square:
    """Creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of a square and its position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the size"""
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        """Getter  of the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of the position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area"""
        return self.__size**2

    def my_print(self):
        """Prints out the square with #'s"""
        if self.__size != 0:
            for new_line in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print()
