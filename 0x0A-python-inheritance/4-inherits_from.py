#!/usr/bin/python3
"""instantiation of a function that returns true if
an object is a subclass of another and false if not"""


def inherits_from(obj, a_class):
    """returns true if an object is a subclass of another and false if not"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
