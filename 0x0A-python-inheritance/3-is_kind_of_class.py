#!/usr/bin/python3
"""instantiation of a function that returns true if
an object is an instance and False if not"""


def is_kind_of_class(obj, a_class):
    """returns true if an object is an instance and False if not"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
