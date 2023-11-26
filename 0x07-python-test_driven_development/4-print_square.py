#!/usr/bin/python3

"""this function prints square with the '#' element"""


def print_square(size):

    """function prototype"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            print("#"*size)
