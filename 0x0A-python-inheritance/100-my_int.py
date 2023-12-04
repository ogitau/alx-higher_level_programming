#!/usr/bin/python3
""" My reverse integer module"""


class MyInt(int):
    """class myint inherits from class int"""

    def __eq__(self, other):
        """initialization of self other"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """method calls equal in init super class"""
        return int.__eq__(self, other)
