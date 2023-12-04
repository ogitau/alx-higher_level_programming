#!/usr/bin/python3
"""function that returns true if object is same as its instance
and false if not"""


def is_same_class(obj, a_class):
    """returns true if object is same as its instanceand false if not"""

    if type(obj) == a_class:
        return True
    else:
        return False
