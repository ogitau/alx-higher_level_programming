#!/usr/bin/python3
"""My module for class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """hierachical inheritance from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of an instance of a square"""

        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """update for attributes of Square"""
        attrs_square = ["id", "size", "x", "y"]

        for position_sq, value in enumerate(args):
            if position_sq > (len(attrs_square) - 1):
                break
            setattr(self, attrs_square[position_sq], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """returns string representation of a square"""

        return "[square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    def to_dictionary(self):
        """add to dict"""
        new_dict = {}
        attrs = ["id", "size", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
