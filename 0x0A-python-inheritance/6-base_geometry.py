#!/usr/bin/python3
"""instantiation of an empty class BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class for geographic objects"""
    def area(self):
        raise Exception("area() is not implemented")
