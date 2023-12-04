#!/usr/bin/python3
"""instantiation of Module for geometry"""


class BaseGeometry():
    """the Base class"""
    def area(self):
        """ Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that checks if value is a number and
        if it's an appropriate number"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
