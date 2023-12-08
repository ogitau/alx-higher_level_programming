#!/usr/bin/python3
"""My module for creating a class Base"""
import json
import csv


class Base:
    """the base class for all the classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """assign public instance atttribute id with this argument value"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
